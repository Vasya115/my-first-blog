"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.post_list, name='post_list'),
    path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    path(r'^post/new/$', views.post_new, name='post_new'),
    path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    path(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    path(r'^register/$', views.register, name='register'),
    path(r'^login/$', views.user_login, name='login'),
    path(r'^register/(?P<pk>\d+)/$', views.register, name='register'),
    path(r'^restricted/', views.restricted, name='restricted'),
    path(r'^logout/$', views.user_logout, name='logout'),


]
