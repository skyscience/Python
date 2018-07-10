"""blogpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blogs.views import index, SearchView, blog_list, blog_detail,CommentView
from users.views import LoginView, RegisterView, ActiveView, LogoutView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index' ),
    url(r'^list$', blog_list, name='blog_list'),
    url(r'^search$', SearchView.as_view(), name='search'),
    url(r'^category/(?P<cid>[0-9]+)/$', blog_list),
    url(r'^tags/(?P<tid>[0-9]+)/$', blog_list),
    url(r'^blog/(?P<bid>[0-9]+)/$', blog_detail, name='blog_detail'),
    url(r'^comment/(?P<bid>[0-9]+)$', CommentView.as_view(), name='comment'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<active_code>[a-zA-Z0-9]+)', ActiveView.as_view(), name='active'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
]
