from django.contrib import admin

from MaterialsSystem.settings import status_choices_dict
from .models import *


class ApplicationHistoryInline(admin.TabularInline):
    model = ApplicationHistory
    extra = 0
    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# 审批记录，不允许新增、修改、删除
class ApplicationDetailInline(admin.TabularInline):
    model = ApplicationDetail
    extra = 0


class ApplicationFileInline(admin.TabularInline):
    model = ExApplicationFile
    extra = 0
    fields = ["file"]


@admin.register(ExWarehousingApplication)
class ExWarehousingApplicationAdmin(admin.ModelAdmin):
    list_display = ["title", "applicant", "applicant_user", "des_short", "add_time", "create_user", "status_short"]
    list_filter = ["title", "create_user", "applicant_user"]
    date_hierarchy = "add_time"
    readonly_fields = ["create_user"]
    inlines = [ApplicationFileInline, ApplicationDetailInline, ApplicationHistoryInline]
    fields = ["title", "des"]
    save_as_continue = False
    save_as = False

    def des_short(self, obj):
        if len(obj.des) >= 10:
            return obj.des[:10]

    des_short.short_description = u'领用原因'

    def get_queryset(self, request):
        qs = super(ExWarehousingApplicationAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(seller=request.user.id)


    def status_short(self, obj):

        return status_choices_dict.get(obj.status)

    status_short.short_description = u'申请状态'

    def save_model(self, request, obj, form, change):
        obj.create_user = request.user
        super(ExWarehousingApplicationAdmin, self).save_model(request, obj, form, change)