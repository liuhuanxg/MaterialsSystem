import traceback

import pdfkit
from django.contrib.auth import login as Auth_Login, authenticate, logout as Auth_Logout
from django.http import JsonResponse
from django.shortcuts import Http404
from django.template.response import TemplateResponse
from easy_pdf.views import PDFTemplateView
from MaterialsSystem import settings
from .models import *


# 用于手机端登录
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
            resp["data"] = user
            resp["msg"] = "登录成功"
    except:
        print("login error:", traceback.format_exc())
    return JsonResponse(resp)


# 退出
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
def get_ex_applications(request):
    resp = {"status": 0, "data": [], "msg": ""}
    try:
        params = request.POST
        username = params.get("username")
        applications = ExWarehousingApplication.objects.filter(next_node=username)

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


def do_approval(request):
    resp = {"status": 0, "data": [], "msg": ""}
    try:
        params = request.GET
        _id = params.get("_id")
        print("_id", _id)
        applications = ExWarehousingApplication.objects.filter(id=_id)
        if applications.exists():
            application = applications[0]
            print(application.status)
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
        resp["status"] = 1
        resp["msg"] = "审批成功"
    except:
        print("login error:", traceback.format_exc())
    return JsonResponse(resp)

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class HelloPDFView(PDFTemplateView):
    template_name = 'material_application/outbound_order.html'  # html模板

    # base_url = 'file://' + settings.STATIC_ROOT
    download_filename = 'hello.pdf'  # 下载pdf时的文件名

    def get_context_data(self, **kwargs):
        data = self.request.GET  # 可以获取请求参数
        pdfmetrics.registerFont(TTFont('yh', '%s/static/font/msyh.ttf' % settings.BASE_DIR))
        # DEFAULT_FONT['helvetica'] = 'yh'
        return super(HelloPDFView, self).get_context_data(
            pagesize='A4',
            title='Hi there!',  # 转成pdf后文件上方的标题
            other='other',  # 也可以按需求增加自己需要的值，然后通过django的模板语言渲染到页面上
            **kwargs
        )


def download_ex_application(request):
    try:
        # params = request.GET
        # _id = params.get("_id")
        # ExWarehousingApplication.objects.filter(id=_id)
        # return render(request, "material_application/outbound_order.html")
        t = TemplateResponse(request, 'quotation.html', locals())
        t.render()
        # # print t.content
        # file = pdfkit.html_str(t.content)
        # response = StreamingHttpResponse(file)
        # response['Content-Type'] = 'application/octet-stream'
        # response['Content-Disposition'] = 'attachment;filename="product.pdf"'
        # return response
        pdfkit.from_url('https://www.google.com.hk', 'out1.pdf')
    except:
        raise Http404
