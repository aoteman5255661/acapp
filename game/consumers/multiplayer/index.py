from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
import json
from django.core.cache import cache


class MultiPlayer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = None

        for i in range(1000):
            name = "room-%d" % i
            if not cache.has_key(name) or len(cache.get(name)) < settings.ROOM_CAPACITY:
                self.room_name = name
                break

        print(self.room_name)
        if not self.room_name:
            return

        await self.accept()

        if not cache.has_key(self.room_name):
            print("设置房间号！！")
            cache.set(self.room_name, [], 3600)  # 1h

        print("++++++++++++++++++++")
        for player in cache.get(self.room_name):
            print("发送!!!")
            await self.send(text_data=json.dumps({
                'event': "create_player",
                'uuid': player['uuid'],
                'username': player['username'],
                'photo': player['photo'],
            }))

        # self.room_name = "room"
        await self.channel_layer.group_add(self.room_name, self.channel_name)

    async def disconnect(self, close_code):
        print('disconnect')
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def create_player(self, data):
        players = cache.get(self.room_name)
        players.append({
            "uuid": data['uuid'],
            "username": data["username"],
            "photo": data["photo"],
        })
        cache.set(self.room_name, players, 3600)  # 1h
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': "group_create_player",
                'event': "create_player",
                'uuid': data['uuid'],
                'username': data['username'],
                'photo': data['photo'],
            }
        )

    async def group_create_player(self, data):
        await self.send(text_data=json.dumps(data))

    async def receive(self, text_data):
        print("接收！！   ", text_data)

        data = json.loads(text_data)
        event = data['event']

        if event == "create_player":
            print("创建 用户")
            await self.create_player(data)
        print(data)
