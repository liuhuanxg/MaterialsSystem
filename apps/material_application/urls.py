# -*-coding:utf-8 -*-

from django.urls import path

from .views import *

urlpatterns = [
    path("login/", login),
    path("logout/", logout),
    path("get_ex_applications/", get_ex_applications),
    path("do_approval/", do_approval),

    # 出库单
    path("local_order_pdf/", local_order_pdf),
    path("center_order_pdf/", center_order_pdf),
    # path('pdf/', HelloPDFView.as_view(), name='pdf'),
]

app_name = "material_application"
