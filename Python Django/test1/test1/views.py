from django.http import HttpResponse

def index(request):
    return HttpResponse('index')
def detail(request,id):
    return HttpResponse('detail %s'%id)