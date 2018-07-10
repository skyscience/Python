from django.http import HttpResponse

class MyException():
    def process_exception(request,response, exception):
    return HttpResponse(exception.message)