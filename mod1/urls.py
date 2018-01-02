#from django.shortcuts import render

# Create your views here.
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.post_list, name='post_list'),
    ]
