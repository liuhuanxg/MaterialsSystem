import logging
import os
import traceback
from django.contrib.auth.decorators import login_required
from center_library.models import CenterOutboundOrder, CenterOutboundOrderDetail
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

logger = logging.getLogger("django")


# logger.debug("This is an debug msg")
# logger.info("This is an info msg")
# logger.warning("This is an warning msg")
# logger.error("This is an error msg")

# 用于手机端登录
@login_required
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
        logger.error("login error:{}".format(traceback.format_exc()))
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
        logger.error("logout error:{}".format(traceback.format_exc()))
    return JsonResponse(resp)


# 查看所有待审批列表
@csrf_exempt
def get_ex_applications(request):
    resp = {"status": 0, "data": [], "msg": ""}
    try:
        params = request.POST
        user_id = params.get("user_id")
        applications = ExWarehousingApplication.objects.filter(next_node=user_id).exclude(status="3")
        logger.info("get_ex_applications user_id:{}".format(user_id))
        for application in applications:
            ret_application_details = []
            ret_application_files = []
            application_details = ApplicationDetail.objects.filter(application=application.id)
            for application_detail in application_details:
                ret_application_details.append(
                    {
                        "number": application_detail.number,
                        "type_name": application_detail.type_name.materials_name + "_" + application_detail.type_name.specifications + "_" + application_detail.type_name.unit,
                        "detail_id": application_detail.id,
                    }
                )
            application_files = ExApplicationFile.objects.filter(application=application.id)
            for application_file in application_files:
                ret_application_files.append(
                    {
                        "url": application_file.file.url,
                        "filename": application_file.file.name,
                        "id": application_file.id,
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
                "application_files": ret_application_files,
            }
            resp["data"].append(data)
        resp["status"] = 1
    except:
        logger.error("get_ex_applications error:{}".format(traceback.format_exc()))
    return JsonResponse(resp)


import json


@csrf_exempt
def do_approval(request):
    resp = {"status": 0, "data": [], "msg": ""}
    params = request.POST
    try:
        _id = params.get("_id")
        user_id = params.get("user_id", "")
        application_details = params.get("application_details", "")

        application = ExWarehousingApplication.objects.filter(id=_id, next_node=str(user_id)).first()
        now_user = User.objects.filter(id=user_id).first()
        logger.info("do_approval,_id:{}, user_id:{}, application_details:{}".format(_id, user_id, application_details))
        if not application:
            resp["msg"] = "未查到审批信息"
            return JsonResponse(resp)
        if not now_user:
            resp["msg"] = "未查询到用户信息"
            return JsonResponse(resp)
        action = "通过"

        if application.status == "1":
            application.status = "2"
            user = User.objects.filter(groups__name__contains="局长").first()
            if user:
                application.next_node = user.id
        elif application.status == "2":
            application.status = "3"
            user = User.objects.filter(groups__name__contains="主管科室").first()
            if user:
                application.next_node = user.id
        application.save()
        if application_details:
            application_details = json.loads(application_details)
            for application_detail in application_details:
                ApplicationDetail.objects.filter(id=application_detail.get("detail_id", ""), application_id=_id).update(
                    number=application_detail.get("number", ""))
        resp["status"] = 1
        resp["msg"] = "审批成功"
        ApplicationHistory.objects.create(
            application_id=_id,
            application_user=now_user.first_name,
            action=action
        )
    except:
        logger.error("do_approval error:{},params:{}".format(traceback.format_exc(), params))
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

    context["approval_historys"] = {
        "user1": {
            "first_name": "申报人手签",
            "path": "/media/user_font/申报人手签.jpg",
            "date": "2022-08-30"
        }
    }
    font_patch()
    html = template.render(context)
    status = pisa.CreatePDF(html,
                            dest=response,
                            link_callback=os.path.join(settings.BASE_DIR, "docs", "建库流程1.pdf"))

    if status.err:
        logger.error("center_order_pdf status:{}".format(status.err))
        response = render(request, html_path, {
            "order": context["order"],
            "order_details": context["order_details"],
            "historys_details": context["historys_details"],
        })
    return response
