from django.conf.urls import include,url
from test4 import urls
urlpatterns = [
    url(r'^',include('app1.urls')),
]
