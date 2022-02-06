from django.http import JsonResponse
from game.models.player.player import Player


def getinfo_accaap(request):
    player = Player.objects.all()[0]
    return JsonResponse({
        'result': "success",
        'username': player.user.username,
        'photo': player.photo,
    })


def getinfo_web(request):
    player = Player.objects.all()[0]
    print("hhhhhh")
    return JsonResponse({
        'result': "success",
        'username': player.user.username,
        'photo': player.photo,
    })


def getinfo(request):
    print("zzzzzz")
    platform = request.GET.get("platform")
    if platform == "ACAPP":
        return getinfo_accaap(request)
    elif platform == "WEB":
        return getinfo_web(request)
