from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
import json
from django.core.cache import cache

class MultiPlayer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = None

        for i in range(1000):
            name = "room-%d" % (i)
            if not cache.has_key(name) or len(cache.get(name)) < settings.ROOM_CAPACITY:
                self.room_name = name
                break

        if not self.room_name:
            return

        await self.accept()
        if not cache.has_key(self.room_name):
            cache.get(self.room_name, [], 3600)  # 1h

        for player in cache.get(self.room_name):
            await self.send(text_data=json.dumps({
                'event', "create_player",
                'uuid': player['uuid'],
                'username': player['username'],
                'photo': player['photo'],
            }))

        self.room_name = "room"
        await self.channel_layer.group_add(self.room_name, self.channel_name)

    async def disconnect(self, close_code):
        print('disconnect')
        await self.channel_layer.group_discard(self.room_name, self.channel_name);

    async def create_player(self, data):
        players = cahce.get(self.room_name)
        players.append({
            "uuid": data['uuid'],
            "username": data["username"],
            "photo": data["photo"],
        })
        cache.set(self.room_name, player, 3600) #1h

    async def receive(self, text_data):
        data = json.loads(text_data)
        event = data['event']

        if event == "create player":
            await self.create_player(data)
        print(data)

