

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from test1 import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include('booktest.urls')),
    # url(r'^admin/', include(admin.site.urls, namespace='booktest')),
    url(r'^book/([0-9]+)/$', views.detail)
]
