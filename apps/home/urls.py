# -*-coding:utf-8 -*-

from django.urls import path

from .views import *

urlpatterns = [
    path("add_types/", add_types)
]

app_name = "home"
