from django.shortcuts import render
from .models import Bookinfo


def index(request):
    book = Bookinfo.objects.all()
    cd = len(book)
    print('=======================1 >>>',book)

    context = {'book' : book,'len':cd} 
    print('=======================2 >>>',book)
    print('=======================3 >>>',context)
    return render(request,'booktest/index.html',context)


def detail(request, id):
    book = Bookinfo.objects.get(pk=id)
    context = {'book' : book, 'date':book.bdate}    
    print('//////////////////////////////////// 1 >>>')
    print('//////////////////////////////////// 2 >>>')
    return render(request,'booktest/detail.html',context)