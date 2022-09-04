# -*-coding:utf-8 -*-

from django.urls import path

from .views import *

urlpatterns = [
    path("index/", my_index)
]

app_name = "home"
