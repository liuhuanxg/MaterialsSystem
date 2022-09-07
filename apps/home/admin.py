from django.apps import apps
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.http import HttpResponse
from django.shortcuts import redirect
from local_library.models import SupplierMessage
from openpyxl import Workbook

from .models import *

# 任丘市
admin.site.site_header = '任丘市防疫物资管理'
admin.site.site_title = '任丘市防疫物资管理'

# 指定首页导航顺序
apps_indexes = {
    "local_library": [
        "SupplierMessage",
        "LocalLibrary",
        "LocalLabraryMaterials",
        "LocalOutboundOrder",
    ],

    "center_library": [
        "CenterLibrary",
        "CenterWarehousingApplication",
        "CenterLabraryQuantity",
        "CenterOutboundOrder",
    ],

    "home": [
        "MaterialsType",
    ],
    "material_application": [
        "ExWarehousingApplication",
        "Accounts",
    ]
}


def find_app_index(app_label):
    app = apps.get_app_config(app_label)
    main_menu_index = getattr(app, 'main_menu_index', 9999)
    return main_menu_index


def index_decorator(func):
    def inner(*args, **kwargs):
        templateresponse = func(*args, **kwargs)
        app_list = templateresponse.context_data['app_list']
        app_list.sort(key=lambda r: find_app_index(r['app_label']))
        for app in app_list:
            apps_index = apps_indexes.get(app["app_label"])
            if apps_index:
                # 按照指定顺序排序
                models = app["models"]
                new_models = []
                for i in models:
                    model_name = i["object_name"]
                    if model_name in apps_index:
                        pos = apps_index.index(model_name)
                        new_models.append({"pos": pos, "model": i})
                    else:
                        new_models.append({"pos": 99, "model": i})
                new_models.sort(key=lambda s: s["pos"])
                models = [x["model"] for x in new_models]
                app["models"] = models
        return templateresponse

    return inner


admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)


@admin.register(MaterialsType)
class LocalMaterialsTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "materials_name", "unit", "specifications", "add_time", "add_date", "modify_time"]
    list_filter = ["materials_name"]
    date_hierarchy = "add_date"
    fields = ["materials_name", "specifications", "unit", "warning_quantity"]
    search_fields = ["materials_name", "specifications"]
    actions = ['make_published']

    # @admin.action(description='下载模板')
    def make_published(self, request, queryset):
        records = list(queryset.values())
        #  数据库的英文字段和中文字段的映射字典
        zh_en = {
            '物料名称': 'materials_name',
            '规格': 'specifications',
            '单位': 'unit',
        }
        zh = list(zh_en.keys())
        zh.extend(["单价(元)"])
        records_list = [zh]
        for r in records:
            data = [r[zh_en[k]] for k in zh if k in zh_en]
            records_list.append(data)
        #  开始批量写入数据
        wb = Workbook()
        ws = wb.active
        for row in records_list:
            ws.append(row)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename="物料模板.xlsx"'
        wb.save(response)
        return response

    make_published.short_description = u'下载模板'


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ["username", "first_name", "email", "is_staff", "is_active", "is_superuser", "user_groups"]

    def user_groups(self, obj):
        groups = obj.groups.all()
        groups_name = ""
        for group in groups:
            groups_name = groups_name + "," if groups_name else groups_name
            groups_name = groups_name + group.name
        return groups_name

    user_groups.short_description = u'角色'

    def response_add(self, request, obj, post_url_continue=None):
        if "_addanother" not in request.POST and auth_admin.IS_POPUP_VAR not in request.POST:
            request.POST = request.POST.copy()
            request.POST["_continue"] = 1
        return super().response_add(request, obj, post_url_continue)

    def save_model(self, request, obj, form, change):
        ret = super(UserAdmin, self).save_model(request, obj, form, change)
        # 添加的角色属于供应商时添加或者修改供应商信息
        user_id = obj.id
        user = User.objects.filter(id=user_id)
        if user.exists():
            user = user[0]
            groups = user.groups.filter(name="供应商")
            if groups.exists():
                supplier_message = SupplierMessage.objects.filter(user=obj)
                if supplier_message.exists():
                    supplier_message = supplier_message[0]
                else:
                    supplier_message = SupplierMessage()
                    supplier_message.user = obj
                    supplier_message.save()
                ret = redirect("/local_library/suppliermessage/{}/change/".format(supplier_message.id))
        return ret

    def response_change(self, request, obj):
        if "_addanother" not in request.POST and auth_admin.IS_POPUP_VAR not in request.POST:
            request.POST = request.POST.copy()
            request.POST["_continue"] = 1
        ret = super().response_change(request, obj)

        # 添加的角色属于供应商时添加或者修改供应商信息
        user_id = obj.id
        user = User.objects.filter(id=user_id)
        if user.exists():
            user = user[0]
            groups = user.groups.filter(name="供应商")
            if groups.exists():
                supplier_message = SupplierMessage.objects.filter(user=obj)
                if supplier_message.exists():
                    supplier_message = supplier_message[0]
                else:
                    supplier_message = SupplierMessage()
                    supplier_message.user = obj
                    supplier_message.save()
                ret = redirect("/local_library/suppliermessage/{}/change/".format(supplier_message.id))
        return ret

    def change_view(self, request, object_id, form_url="", extra_context=None):
        if object_id:
            return super(UserAdmin, self).change_view(request, object_id, form_url, extra_context)

    def get_queryset(self, request):
        user = request.user
        qs = super(UserAdmin, self).get_queryset(request)
        if not user.is_superuser:
            qs = qs.filter(id=user.id)
        return qs