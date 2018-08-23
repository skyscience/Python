from .models import BookInfo
from django.shortcuts import render
from django.http import HttpResponse


def page_not_found(request):
    return render_to_response('404.html')


def page_not_found1(request):
    return render_to_response('500.html')

def index(request):
    book = BookInfo.objects.all()
    cd = len(book)
    context = {'book_info' : book,'len':cd} 
    return render(request,'booktest/index.html',context)


def detail(request,id):
    book = BookInfo.objects.get(pk=id)
    context = {'book' : book}
    return render(request,'booktest/detail.html',context)