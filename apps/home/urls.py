# -*-coding:utf-8 -*-

from django.urls import path

from .views import *

urlpatterns = [
    path("my_index/", my_index)
]

app_name = "home"
