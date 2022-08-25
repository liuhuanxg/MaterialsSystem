from django.contrib import admin
from django.utils.html import format_html
from home.models import CodeNumber

from MaterialsSystem.settings import status_choices_dict
from utils.date_utils import get_date_str
from .models import *


# 审批记录，不允许新增、修改、删除
class ApplicationHistoryInline(admin.TabularInline):
    model = ApplicationHistory
    extra = 0

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# 审批详情
class ApplicationDetailInline(admin.TabularInline):
    model = ApplicationDetail
    extra = 0
    fields = ["type_name", "number"]

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


# 申请时上传的附件
class ApplicationFileInline(admin.TabularInline):
    model = ExApplicationFile
    extra = 0
    fields = ["file"]


# 地方库研判详情
class LocalAssessmentDetailInline(admin.TabularInline):
    model = LocalAssessmentDetail
    extra = 0
    fields = ["library_name", "number"]


# 中央库研判详情
class CenterAssessmentDetailInline(admin.TabularInline):
    model = CenterAssessmentDetail
    extra = 0
    fields = ["library_name", "number"]


@admin.register(ExWarehousingApplication)
class ExWarehousingApplicationAdmin(admin.ModelAdmin):
    list_display = ["app_code", "title", "applicant", "applicant_user", "add_time",
                    "status_short", "next_node"]
    list_filter = ["title", "create_user", "applicant_user"]
    date_hierarchy = "add_time"
    readonly_fields = ["create_user"]

    fields = [("title", "des"), ("applicant", "applicant_user"), ("add_time",)]
    db_name = "ExWarehousingApplication"
    change_form_template = "common/ex_app_change_form.html"

    # def des_short(self, obj):
    #     if len(obj.des) >= 10:
    #         return obj.des[:10]
    #
    # des_short.short_description = u'领用原因'

    # def get_queryset(self, request):
    #     qs = super(ExWarehousingApplicationAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(next_node=request.user.id)

    def get_inlines(self, request, obj):
        user = request.user
        inlines = [ApplicationFileInline, ApplicationDetailInline]
        print(str(obj.status))
        print(user.groups.filter(name__contains="主管科室").exists())
        if str(obj.status) == "3" and user.groups.filter(name__contains="主管科室").exists():
            inlines.extend([LocalAssessmentDetailInline, CenterAssessmentDetailInline])
        if obj.next_node != "":
            inlines.append(ApplicationHistoryInline)
        return inlines

    def status_short(self, obj):
        return status_choices_dict.get(obj.status)

    status_short.short_description = u'申请状态'

    def app_status_short(self, obj):
        return format_html(
            '<a href="{}?_id={}">{}</a>'.format("/material_application/do_approval/", obj.id, "点击审批", )
        )

    app_status_short.short_description = u'申请状态'

    # def get_list_display(self, request):
    #     list_display = self.list_display
    #     user = request.user
    #     is_approve = user.groups.filter(Q(name="分管领导") | Q(name="局长"))
    #     if is_approve:
    #         list_display = ["app_code", "title", "applicant", "applicant_user", "add_time",
    #                         "app_status_short", "next_node"]
    #     return list_display

    # def save_formset(self, request, form, formset, change):
    #     if change:
    #         for inline_form in formset.forms:
    #             if inline_form._meta.model == ApplicationDetail and inline_form.has_changed():
    #                 for name, bf in inline_form._bound_items():
    #                     if name == "number" and bf._has_changed():
    #                         new_number = inline_form.instance.number
    #                         old_number = bf.initial
    #                         # if new_number > old_number:
    #
    #     super(ExWarehousingApplicationAdmin, self).save_formset(request, form, formset, change)

    def save_model(self, request, obj, form, change):
        # if "_continue" not in request.POST:
        print("_continue" in request.POST)
        if obj.app_code == "":
            user = User.objects.filter(groups__name__icontains="分管领导").first()
            if user:
                next_node = user.id
            else:
                admin = User.objects.filter(username__icontains="admin").first()
                if admin:
                    next_node = admin.id
                else:
                    next_node = request.user.id
            obj.next_node = next_node
            obj.create_user = request.user
            obj.app_code = CodeNumber.get_app_code(self.db_name)
            date_str = get_date_str()
            code_number = CodeNumber.objects.filter(date_str=date_str, db_name=self.db_name).first()
            if code_number:
                number = code_number.number + 1
                code_number.number = number
                code_number.save()
            else:
                number = 1
                CodeNumber.objects.create(date_str=date_str, db_name=self.db_name, number=number)
            ApplicationHistory.objects.get_or_create(
                application=obj.id,
                application_user=user.first_name,
                action="发起审批"
            )
        elif obj.next_node == str(request.user.id):
            if obj.status == "1":
                obj.status = "2"
                user = User.objects.filter(groups__name__contains="局长").first()
                if user:
                    obj.next_node = user.id
                    ApplicationHistory.objects.get_or_create(
                        application=obj.id,
                        application_user=user.first_name,
                        action="通过"
                    )
            elif obj.status == "2":
                obj.status = "3"
                user = User.objects.filter(groups__name__contains="主管科室").first()
                if user:
                    obj.next_node = user.id
                    ApplicationHistory.objects.get_or_create(
                        application=obj.id,
                        application_user=user.first_name,
                        action="通过"
                    )
            elif obj.status == "3":
                obj.status = "4"
                user = User.objects.filter(groups__name__contains="仓库管理员").first()
                if user:
                    obj.next_node = user.id
                    ApplicationHistory.objects.get_or_create(
                        application=obj.id,
                        application_user=user.first_name,
                        action="通过"
                    )
            elif obj.status == "5":
                obj.status = "6"
                user = User.objects.filter(groups__name__contains="仓库管理员").first()
                if user:
                    obj.next_node = user.id
                    ApplicationHistory.objects.get_or_create(
                        application=obj.id,
                        application_user=user.first_name,
                        action="通过"
                    )
            # obj.save()
        super(ExWarehousingApplicationAdmin, self).save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        return super(ExWarehousingApplicationAdmin, self).response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        return super(ExWarehousingApplicationAdmin, self).response_change(request, obj)

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        if object_id:
            extra_context = extra_context if extra_context else {}
            user = request.user
            print(user.id)
            print(ExWarehousingApplication.objects.get(id=object_id).next_node)
            if str(user.id) == ExWarehousingApplication.objects.get(id=object_id).next_node:
                extra_context["can_approve"] = True
                extra_context["ex_app_id"] = object_id
            else:
                extra_context["can_approve"] = False
                extra_context["ex_app_id"] = object_id
        return super(ExWarehousingApplicationAdmin, self).changeform_view(request, object_id, form_url, extra_context)

# @admin.register(Assessments)
# class AssessmentsAdmin(admin.ModelAdmin):
#     list_display = ["application", "title", "applicant"]
