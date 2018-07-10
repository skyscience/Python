from django.shortcuts import render
from django.http import JsonResponse
from models import AreaInfo

def index(request):
    return render(request, 'ct1/index.html')

def getArea1(request):
    list = AreaInfo.objects.filter(aPArea__isnull=True)
    list2 = []
    for a in list:
        list2.append([a.aid, a.atitle])
    return JsonResponse({'data': list2})

def getArea2(request, pid):
    list = AreaInfo.objects.filter(aPArea_id=pid)
    list2 = []
    for a in list:
        list2.append({'id': a.aid, 'title': a.atitle})
    return JsonResponse({'data': list2})