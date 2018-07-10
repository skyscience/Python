from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$',views.index),
    url(r'^abc/$', views.getArea1),
    url(r'^([0-9]+)/$', views.getArea2),
]