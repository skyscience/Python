from django.conf.urls import url,include
from test3 import urls

urlpatterns = [
    url(r'^',include('booktest.urls'))
]
