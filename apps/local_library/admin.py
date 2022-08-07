from django.apps import apps
from django.contrib import admin

admin.site.site_header = '防疫物资管理'
admin.site.site_title = '防疫物资管理'

# 指定导航顺序
apps_index = []


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
            if app["app_label"] == "local_library":
                # 按照指定顺序排序
                models = app["models"]
                new_models = []
                for i in models:
                    model_name = i["object_name"]
                    pos = apps_index.index(model_name)
                    new_models.append({"pos": pos, "model": i})
                new_models.sort(key=lambda s: s["pos"])
                models = [x["model"] for x in new_models]
                app["models"] = models
        return templateresponse

    return inner


admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)
