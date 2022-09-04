# -*-coding:utf-8 -*-

from django.urls import path

from .views import *

urlpatterns = [
    path("login/", login),
    path("logout/", logout),
    path("get_ex_applications/", get_ex_applications),
    path("do_approval/", do_approval),

    # 出库单
    path("test_download_pdf/", test_download_pdf),
    path("center_order_html/", center_order_html),
    path("local_order_html/", local_order_html),
    path("download_order_pdf/", download_order_pdf),
]

app_name = "material_application"
