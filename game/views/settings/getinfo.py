#  -*-  coding:utf-8  -*-
from django.http import JsonResponse
from game.models.player.player import Player
from django.contrib import auth
import sys


def getinfo_accaap(request):
    player = Player.objects.all()[0]
    return JsonResponse({
        'result': "success",
        'username': player.user.username,
        'photo': player.photo,
    })


def getinfo_web(request):
    user = request.user
    # print(request)
    print("user::: {}".format(user))
    # print("is_authen :::: ", user.is_authenticated)
    print("jjjjjj")
    print(user.is_authenticated)
    if not user.is_authenticated:
        print("wei deng lu !!")
        return JsonResponse({
            "result": "未登录"
        })
    else:
        print("yi deng lu")
        player = Player.objects.get(user=user)
        return JsonResponse({
            'result': "success",
            'username': player.user.username,
            'photo': player.photo,
        })


def getinfo(request):
    print('zzzzzz')
    platform = request.GET.get("platform")
    if platform == "ACAPP":
        return getinfo_accaap(request)
    elif platform == "WEB":
        return getinfo_web(request)
