import os
import traceback

from center_library.models import CenterOutboundOrder, CenterOutboundOrderDetail, CenterOutboundOrderHistory
from django.contrib.auth import login as Auth_Login, authenticate, logout as Auth_Logout
from django.http import HttpResponse
from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from local_library.models import LocalOutboundOrder, LocalOutboundOrderHistory, LocalOutboundOrderDetail
from xhtml2pdf import pisa

from MaterialsSystem import settings
from .models import *


# 用于手机端登录
@csrf_exempt
def login(request):
    resp = {"status": 0, "data": {}, "msg": ""}
    try:
        params = request.POST
        username = params.get("username")
        password = params.get("password")
        user = authenticate(username=username, password=password)
        if user:
            Auth_Login(request, user)
            resp["status"] = 1
            resp["data"]["username"] = user.username
            resp["data"]["name"] = user.first_name
            resp["data"]["user_id"] = user.id
            resp["msg"] = "登录成功"
    except:
        print("login error:", traceback.format_exc())
    return JsonResponse(resp)


# 退出
@csrf_exempt
def logout(request):
    Auth_Logout(request)
    resp = {"status": 0, "data": {}, "msg": ""}
    try:
        Auth_Logout(request)
        resp["status"] = 1
        resp["msg"] = "退出成功"
    except:
        print("login error:", traceback.format_exc())
    return JsonResponse(resp)


# 查看所有待审批列表
@csrf_exempt
def get_ex_applications(request):
    resp = {"status": 0, "data": [], "msg": ""}
    try:
        params = request.POST
        user_id = params.get("user_id")
        applications = ExWarehousingApplication.objects.filter(next_node=user_id)
        for application in applications:
            ret_application_details = []
            application_details = ApplicationDetail.objects.filter(application=application.id)

            for application_detail in application_details:
                ret_application_details.append(
                    {
                        "number": application_detail.number,
                        "type_name": application_detail.type_name.materials_name,
                    }
                )
            data = {
                "_id": application.id,
                "title": application.title,
                "applicant": application.applicant,
                "applicant_user": application.applicant_user,
                "des": application.des,
                "add_time": application.add_time,
                "add_date": application.add_date,
                "application_details": ret_application_details,
            }
            resp["data"].append(data)
        resp["status"] = 1
    except:
        print("login error:", traceback.format_exc())
    return JsonResponse(resp)


@csrf_exempt
def do_approval(request):
    resp = {"status": 0, "data": [], "msg": ""}
    try:
        params = request.POST
        _id = params.get("_id")
        user_id = params.get("user_id", "")
        if not _id or not params:
            resp["msg"] = "请先登录。"
            return JsonResponse(resp)
        action = "通过"
        user = None
        applications = ExWarehousingApplication.objects.filter(id=_id)
        if applications.exists():
            application = applications[0]
            print(application.status)
            if application.status == "1":
                application.status = "2"
                user = User.objects.filter(groups__name__contains="局长", id=user_id).first()
                if user:
                    application.next_node = user.id
            elif application.status == "2":
                application.status = "3"
                user = User.objects.filter(groups__name__contains="主管科室", id=user_id).first()
                if user:
                    application.next_node = user.id
            application.save()
        if user:
            resp["status"] = 1
            resp["msg"] = "审批成功"
            ApplicationHistory.objects.create(
                application_id=_id,
                application_user=user.first_name,
                action=action
            )
    except:
        print("login error:", traceback.format_exc())
    return JsonResponse(resp)


def font_patch():
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfbase import pdfmetrics
    from xhtml2pdf.default import DEFAULT_FONT
    pdfmetrics.registerFont(TTFont('yh', '{}/font/msyh.ttf'.format(
        settings.STATICFILES_DIRS[0])))
    DEFAULT_FONT['helvetica'] = 'yh'


# 本地库出库单pdf文件
def local_order_pdf(request):
    object_id = request.GET.get("object_id")

    order = LocalOutboundOrder.objects.filter(id=object_id).first()
    if not order:
        raise Http404
    response = HttpResponse(content_type="application/pdf")
    html_path = "local_library/local_out_bound_order_change_form_pdf.html"
    template = get_template(html_path)
    order_details = LocalOutboundOrderDetail.objects.filter(app_code_id=object_id)
    historys_details = LocalOutboundOrderHistory.objects.filter(application_id=object_id)
    context = {
        "order": {
            "user": order.user.suppliermessage.company_name,
            "app_code": order.app_code,
            "applicant": order.applicant,
            "applicant_user": order.applicant_user,
            "des": order.des,
            "total_price": order.total_price,
            "add_time": order.add_time,
            "add_date": order.add_date,
        },
        "order_details": [],
        "historys_details": [],

    }
    for order_detail in order_details:
        context["order_details"].append(
            {
                "library_name": order_detail.assessment_detail.library_name.type_name.materials_name,
                "number": order_detail.assessment_detail.number,
                "total_price": order_detail.total_price,
            }
        )

    for historys_detail in historys_details:
        context["historys_details"].append(
            {
                "application_user": historys_detail.application_user,
                "action": historys_detail.action,
                "add_time": historys_detail.add_time,
                "font": "签字",
            }
        )
    font_patch()
    html = template.render(context)
    status = pisa.CreatePDF(html,
                            dest=response,
                            link_callback=os.path.join(settings.BASE_DIR, "docs", "建库流程1.pdf"))

    if status.err:
        response = render(request, html_path, {
            "order": context["order"],
            "order_details": context["order_details"],
            "historys_details": context["historys_details"],
        })
    return response


# 中央库出库单pdf文件
def center_order_pdf(request):
    object_id = request.GET.get("object_id")

    order = CenterOutboundOrder.objects.filter(id=object_id).first()
    if not order:
        raise Http404
    response = HttpResponse(content_type="application/pdf")
    html_path = "local_library/local_out_bound_order_change_form_pdf.html"
    template = get_template(html_path)
    order_details = CenterOutboundOrderDetail.objects.filter(app_code_id=object_id)
    historys_details = CenterOutboundOrderHistory.objects.filter(application_id=object_id)
    context = {
        "order": {
            "app_code": order.app_code,
            "applicant": order.applicant,
            "applicant_user": order.applicant_user,
            "des": order.des,
            "total_price": order.total_price,
            "add_time": order.add_time,
            "add_date": order.add_date,
        },
        "order_details": [],
        "historys_details": [],

    }
    for order_detail in order_details:
        context["order_details"].append(
            {
                "library_name": order_detail.assessment_detail.library_name.type_name.materials_name,
                "number": order_detail.assessment_detail.number,
                "total_price": order_detail.total_price,
            }
        )

    for historys_detail in historys_details:
        context["historys_details"].append(
            {
                "application_user": historys_detail.application_user,
                "action": historys_detail.action,
                "add_time": historys_detail.add_time,
                "font": "签字",
            }
        )
    font_patch()
    html = template.render(context)
    status = pisa.CreatePDF(html,
                            dest=response,
                            link_callback=os.path.join(settings.BASE_DIR, "docs", "建库流程1.pdf"))

    if status.err:
        response = render(request, html_path, {
            "order": context["order"],
            "order_details": context["order_details"],
            "historys_details": context["historys_details"],
        })
    return response
