from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^area1/$', views.getArea1),
    url(r'^([0-9]+)/$', views.getArea2),
]