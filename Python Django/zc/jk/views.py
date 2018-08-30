from django.shortcuts import render
from django.http import request
from time import sleep

def open(request,len1):
    print('[]',len1)
    len1 += 1
    context = {'len':len1}
    return render(request,'jk/index.html',context)


def jk(request):
    a = 10
    while True:
        sleep(0.8)
        open(request, a)