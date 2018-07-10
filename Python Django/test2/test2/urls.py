
from django.contrib import admin
from django.conf.urls import url,include
from . import views
from test2 import urls

urlpatterns = [
    # path('admin/', admin.site.urls),  #管理界面
    # url(r'^$',views.index),  #什么都不加进入index
    # url(r'^([0-9]+)/$',views.detail) #将地址值传给detail
    url(r'^',include('booktest.urls')) #任何值都进入booktest的urls
]



