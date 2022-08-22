from django.apps import apps
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.shortcuts import redirect
from .models import *

admin.site.site_header = '任丘市防疫物资管理'
admin.site.site_title = '任丘市防疫物资管理'

# 指定导航顺序
apps_indexes = {
    "local_library": ["LocalLibrary",
                      "LocalLibraryBudget",
                      "WarehousingApplication",
                      "LocalLabraryMaterials",
                      # "LocalLibraryFile"
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
    list_display = ["materials_name", "unit", "specifications", "add_time", "add_date", "modify_time"]
    list_filter = ["materials_name"]
    date_hierarchy = "add_date"
    fields = ["materials_name", "specifications", "unit", "warning_quantity"]

    # def save_model(self, request, obj, form, change):
    #     obj.create_user = request.user
    #     super(LocalMaterialsTypeAdmin, self).save_model(request, obj, form, change)


# @admin.register(CodeNumber)
# class CodeNumberAdmin(admin.ModelAdmin):
#     list_display = ["number", "db_name", "date_str"]


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ["username", "first_name", "email", "is_staff", "is_active", "is_superuser"]

    # def save_model(self, request, obj, form, change):
    #     obj.create_user = request.user
    #     super(LocalMaterialsTypeAdmin, self).save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        if "_addanother" not in request.POST and auth_admin.IS_POPUP_VAR not in request.POST:
            request.POST = request.POST.copy()
            request.POST["_continue"] = 1
        print("post_url_continue", post_url_continue)
        return super().response_add(request, obj, post_url_continue)

    def save_model(self, request, obj, form, change):
        super(UserAdmin, self).save_model(request, obj, form, change)
        return redirect("/local_library/suppliermessage/1/change/")

    def response_change(self, request, obj):
        if "_addanother" not in request.POST and auth_admin.IS_POPUP_VAR not in request.POST:
            request.POST = request.POST.copy()
            request.POST["_continue"] = 1
        super().response_change(request, obj)
        return redirect("/local_library/suppliermessage/1/change/")

    def change_view(self, request, object_id, form_url="", extra_context=None):
        if object_id:
            return super(UserAdmin, self).change_view(request, object_id, form_url, extra_context)

    # return redirect("/local_library/suppliermessage/1/change/")
