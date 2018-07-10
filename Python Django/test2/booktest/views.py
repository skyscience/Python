from .models import BookInfo
from django.shortcuts import render

def index(request):
    booklist = BookInfo.objects.all()
    return render(request,'booktest/index.html')

def detail(reqeust,id):
    book = BookInfo.objects.get(pk=id)
    context = {'book': book}
    return render(reqeust,'booktest/detail.html',context)
    
def det(reqeust,id):
    return HttpRespinse("det %s"%id)