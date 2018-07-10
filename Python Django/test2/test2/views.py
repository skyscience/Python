from django.http import HttpResponse
def index(reqeust):
    return HttpResponse("index")
def detail(reqeust,id):
    return HttpResponse("detail %s"%id)


'''
from django.shortcuts import render

def index(reqeust):
    booklist = BookInfo.objects.all()
    return render(reqeust, 'booktest/index.html', {'booklist': booklist})


def detail(reqeust, id):
    book = BookInfo.objects.get(pk=id)
    return render(reqeust, 'booktest/detail.html', {'book': book})
    '''