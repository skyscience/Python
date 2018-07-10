from django.conf.urls import url
from . import views,views1

urlpatterns = [
    url(r'^$', views1.index, name='index'),
    # url(r'^$',views.index),
    url(r'^([0-9]+)/$',views.det)
]




