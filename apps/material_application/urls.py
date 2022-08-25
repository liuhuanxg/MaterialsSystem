#-*-coding:utf-8 -*-

from django.urls import path, include, re_path
from .views import *
from django.contrib import admin


urlpatterns = [
    path("do_approval/", do_approval),
    path("download_ex_application/", download_ex_application),
    path('pdf/', HelloPDFView.as_view(), name='pdf'),
]

app_name = "material_application"