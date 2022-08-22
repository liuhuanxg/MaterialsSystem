import traceback

from django.contrib.auth import login as Auth_Login, authenticate, logout as Auth_Logout
from django.http import JsonResponse

from .models import ExWarehousingApplication, ApplicationDetail


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
        params = request.POST
        _id = params.get("_id")
        applications = ExWarehousingApplication.objects.filter(id=_id)
        if applications.exists():
            application = applications[0]
            application.next_node = ""
            application.save()
        resp["status"] = 1
    except:
        print("login error:", traceback.format_exc())
    return JsonResponse(resp)