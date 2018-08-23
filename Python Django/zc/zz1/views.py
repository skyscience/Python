from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo

def index(request):
    info = BookInfo.objects.all()
    cd = len(info)
    

    # 求和
    sum = 0
    c = 1600
    for i in info:
        sum += i.money  
    b = sum/1600*100
    b = int(b)


    color = 'danger'
    if b > 30:
        color = 'warning'
    if b > 50:
        color = 'info'
    if b > 70:
        color = 'success'

    # print('>>>>>>>>>>>  1')
    # print('>>>>>>>>>>>  2')
    # print('>>>>>>>>>>>  3')
    # print('>>>>>>>>>>>  4')

    context = {'player' : info,'len':cd, 'sum': sum, 'bfb':b, 'color':color}
    return render(request,'zc/index.html',context)

def detail(request, id):
    return HttpResponse('detail %s'%id)