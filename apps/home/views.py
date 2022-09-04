from django.http import HttpResponseRedirect
from django.contrib.admin.sites import AdminSite, site
from django.template.response import TemplateResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from material_application.models import ExWarehousingApplication
from material_application.admin import ExWarehousingApplicationAdmin
from local_library.models import LocalOutboundOrder

class MySite(AdminSite):
    @never_cache
    def index(self, request, extra_context=None):
        """
        Display the main admin index page, which lists all of the installed
        apps that have been registered in this site.
        """
        app_list = self.get_app_list(request)

        context = {
            **self.each_context(request),
            'title': self.index_title,
            'app_list': app_list,
            **(extra_context or {}),
        }
        print("context:{}".format(context))
        request.current_app = self.name

        return TemplateResponse(request, self.index_template or 'admin/index.html', context)


@csrf_exempt
def my_index(request):
    user = request.user
    is_supplier = user.groups.filter(name="供应商").first()
    to_do_list = []
    to_do_list_headers = []
    # 查询待处理事项
    if is_supplier:
        is_supplier = True
        local_outbounder_orders = LocalOutboundOrder.objects.filter(user_id=user.id)
    else:
        is_supplier = False
        to_do_list_headers = [
            "申请单号",
            "申请主题",
            "申请单位",
            "领用人",
            "状态",
            "申请日期",
        ]
        ex_warehousing_applications = ExWarehousingApplication.objects.filter(next_node=user.id)

        for ex_warehousing_application in ex_warehousing_applications:
            to_do_list.append(
                {
                    # "_id": ex_warehousing_application.id,
                    "app_code": ex_warehousing_application.app_code,
                    "title": ex_warehousing_application.title,
                    "applicant": ex_warehousing_application.applicant,
                    "applicant_user": ex_warehousing_application.applicant_user,
                    "status": ex_warehousing_application.status,
                    "add_date": ex_warehousing_application.add_date,
                }
            )

    extra_context = {
        "is_supplier": is_supplier,
        "to_do_list": to_do_list,
        "to_do_list_headers": to_do_list_headers,
    }
    ret = site.index(request, extra_context=extra_context)
    # return HttpResponseRedirect()
    return ret
