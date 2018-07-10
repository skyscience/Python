from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    print('============ index =========')
    return render(request, 'test_2/index.html')
def personal(request):
    print('============ personal =========')
    return render(request, 'test_2/personal.html')
def about(request):
    print('============ about =========')
    return render(request, 'test_2/about.html')
