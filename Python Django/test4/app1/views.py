from django.shortcuts import render
from django.http import JsonResponse
from .models import AreaInfo

def index(request):
    print('============ index =========')
    return render(request, 'index.html')

def getArea1(request):
    print('================list')
    list = AreaInfo.objects.all()
   
    list2 = []
    for a in list:
        list2.append({'aid':a.aid, 'title':a.atitle})
    print(list)
    print(list2)
    return JsonResponse({'data': list2})

def getArea2(request, pid):
    ist = AreaInfo.objects.filter(aPArea_id=pid)
    list2 = []
    for a in list:
        list2.append({'id': a.aid, 'title': a.atitle})
    return JsonResponse({'data': list2})    