from django.conf.urls import url
from . import views
import booktest

urlpatterns = [
    url(r'^$',views.index),
    url(r'^([0-9]+)/$',views.detail),
]

handler404 = booktest.views.page_not_found 
handler500 = booktest.views.page_not_found1