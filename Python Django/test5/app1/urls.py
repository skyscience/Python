from django.conf.urls import url
from . import views
print('=============')
urlpatterns = [
    url(r'i',views.index),
    url(r'p',views.personal),
    url(r'a',views.about)
]