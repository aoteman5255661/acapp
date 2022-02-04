from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    line1 = '<h1 style="text-align:center">我的第一个网页</h1>'
    line2 = '<img src="https://i1.hdslb.com/bfs/archive/ba81e7381ce454263069e2f0be12c740a9df2994.jpg@672w_378h_1c.webp" width=2000>'
    return HttpResponse(line1+line2)


