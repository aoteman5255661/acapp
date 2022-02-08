from django.shortcuts import redirect
from django.core.cache import cache
import requests
from django.contrib.auth.models import User
from game.models.player.player import Player
from django.contrib.auth import login
from random import randint
from django.http import  JsonResponse

def receive_code(request):
    data = request.GET

    if "errcode" in data:
        return JsonResponse({
            "result": "apply fail",
            "errcode": data['errcode'],
            "errmsg": data["errmsg"],
        })

    code = data.get("code")
    state = data.get("state")

    if not cache.has_key(state):
        return JsonResponse({
            "result": "state not exist",
        })
    cache.delete(state)

    apply_access_token_url = "https://www.acwing.com/third_party/api/oauth2/access_token/"
    params = {
        'appid': "1432",
        'secret': "eb6720a5760a43bc9aae942649d1b3f1",
        'code': code,
    }

    access_token_res = requests.get(apply_access_token_url, params=params).json()
    print("access_toke +=================    ", access_token_res)
    access_token = access_token_res['access_token']
    openid = access_token_res['openid']


    players = Player.objects.filter(openid=openid)
    if players.exists():  #如果该用户已存在，则无需重新获取信息，直接登录即可
        login(request, players[0].user)
        return redirect("index")

    get_userinfo_url = "https://www.acwing.com/third_party/api/meta/identity/getinfo"
    params = {
        "access_token": access_token,
        "openid": openid,
    }
    print("params >>>>  ", params)
    userinfo_res = requests.get(url=get_userinfo_url, params=params).json()
    username = userinfo_res['username']
    photo = userinfo_res['photo']

    while User.objects.filter(username=username).exists():
        username += str(randint(0, 9))

    user = User.objects.create(username=username)
    player = Player.objects.create(user=user, photo=photo, openid=openid)

    login(request, user)

    return redirect("index")
