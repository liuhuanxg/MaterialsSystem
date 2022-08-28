# from local_library.models import LocalOutboundOrder
from center_library.models import CenterOutboundOrder, CenterOutboundOrderDetail, CenterOutboundOrderHistory
from django.contrib import admin
from django.shortcuts import HttpResponse
from django.utils.decorators import method_decorator
from django.utils.html import format_html
from django.views.decorators.csrf import csrf_protect
from home.models import CodeNumber
from local_library.models import LocalOutboundOrder, LocalOutboundOrderDetail, LocalOutboundOrderHistory, \
    LocalLabraryMaterials
from openpyxl import Workbook

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


# 申请详情
class ApplicationDetailInline(admin.TabularInline):
    model = ApplicationDetail
    extra = 0
    fields = ["type_name", "number"]

    def has_change_permission(self, request, obj=None):
        # print("has_change_permission self:{},obj:{},obj.status:{}".format(
        #     self, obj, obj.status
        # ))
        if obj and obj.status == "3":
            return False
        return super(ApplicationDetailInline, self).has_change_permission(request, obj)

    def has_add_permission(self, request, obj):
        # print("has_add_permission self:{},obj:{},obj.status:{}".format(
        #     self, obj, obj.status
        # ))
        if obj and obj.status == "3":
            return False
        return super(ApplicationDetailInline, self).has_add_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        # print("has_delete_permission self:{},obj:{},obj.status:{}".format(
        #     self, obj, obj.status
        # ))
        if obj and obj.status == "3":
            return False
        return super().has_delete_permission(request, obj)


# 申请时上传的附件
class ApplicationFileInline(admin.TabularInline):
    model = ExApplicationFile
    extra = 0
    fields = ["file"]

    def has_change_permission(self, request, obj=None):
        # print("has_change_permission self:{},obj:{},obj.status:{}".format(
        #     self, obj, obj.status
        # ))
        if obj and obj.status == "3":
            return False
        return super().has_change_permission(request, obj)

    def has_add_permission(self, request, obj):
        # print("has_add_permission self:{},obj:{},obj.status:{}".format(
        #     self, obj, obj.status
        # ))
        if obj and obj.status == "3":
            return False
        return super().has_add_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        # print("has_delete_permission self:{},obj:{},obj.status:{}".format(
        #     self, obj, obj.status
        # ))
        if obj and obj.status == "3":
            return False
        return super().has_delete_permission(request, obj)


# 地方库研判详情
class LocalAssessmentDetailInline(admin.TabularInline):
    model = LocalAssessmentDetail
    extra = 0
    fields = ["library_name", "number"]

    # 地方库研判，只能选择数量大于0的
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "library_name":
            local_labrary_materials = LocalLabraryMaterials.objects.filter(library_name__is_approve=1)
            kwargs["queryset"] = local_labrary_materials
            kwargs['initial'] = local_labrary_materials.first()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def has_change_permission(self, request, obj=None):
        print("has_change_permission self:{},obj:{},obj.status:{}".format(
            self, obj, obj.status
        ))
        if obj and obj.status == "4":
            return False
        return super().has_change_permission(request, obj)

    def has_add_permission(self, request, obj):
        # print("has_add_permission self:{},obj:{},obj.status:{}".format(
        #     self, obj, obj.status
        # ))
        if obj and obj.status == "4":
            return False
        return super().has_add_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        # print("has_delete_permission self:{},obj:{},obj.status:{}".format(
        #     self, obj, obj.status
        # ))
        if obj and obj.status == "4":
            return False
        return super().has_delete_permission(request, obj)


# 中央库研判详情
class CenterAssessmentDetailInline(admin.TabularInline):
    model = CenterAssessmentDetail
    extra = 0
    fields = ["library_name", "number"]

    def has_change_permission(self, request, obj=None):
        # print("has_change_permission self:{},obj:{},obj.status:{}".format(
        #     self, obj, obj.status
        # ))
        if obj and obj.status == "4":
            return False
        return super().has_change_permission(request, obj)

    def has_add_permission(self, request, obj):
        # print("has_add_permission self:{},obj:{},obj.status:{}".format(
        #     self, obj, obj.status
        # ))
        if obj and obj.status == "4":
            return False
        return super().has_add_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        # print("has_delete_permission self:{},obj:{},obj.status:{}".format(
        #     self, obj, obj.status
        # ))
        if obj and obj.status == "4":
            return False
        return super().has_delete_permission(request, obj)


@admin.register(ExWarehousingApplication)
class ExWarehousingApplicationAdmin(admin.ModelAdmin):
    list_display = ["app_code", "title", "applicant", "applicant_user", "add_time",
                    "status_short", "next_node"]
    list_filter = ["title", "create_user", "applicant_user"]
    date_hierarchy = "add_time"
    readonly_fields = ["create_user"]
    inlines = [ApplicationFileInline, ApplicationDetailInline]
    fields = [("title", "des"), ("applicant", "applicant_user"), ("add_time")]
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
        inlines = self.inlines
        if obj:
            if str(obj.status) == "3" and user.groups.filter(name__contains="主管科室").exists():
                if LocalAssessmentDetailInline not in inlines:
                    inlines.append(LocalAssessmentDetailInline)
                if CenterAssessmentDetailInline not in inlines:
                    inlines.append(CenterAssessmentDetailInline)
            if obj.next_node != "" and ApplicationHistoryInline not in inlines:
                inlines.append(ApplicationHistoryInline)
            print("obj:{}, obj.status:{}, obj.next_node:{}, inlines:{}".format(
                obj, obj.status, obj.next_node, inlines
            ))
        return inlines

    def status_short(self, obj):
        return status_choices_dict.get(obj.status)

    status_short.short_description = u'申请状态'

    def app_status_short(self, obj):
        return format_html(
            '<a href="{}?_id={}">{}</a>'.format("/material_application/do_approval/", obj.id, "点击审批", )
        )

    app_status_short.short_description = u'申请状态'

    def save_formset(self, request, form, formset, change):

        application_id = form.instance.id
        application_status = form.instance.status
        print("form.instance.status:{}, self_id:{}".format(application_status, application_id))
        if change and application_status == "3":
            # 判断研判的数据结果与真实申请是否相等
            flag = False
            all_applications_details = {}
            application_details = ApplicationDetail.objects.filter(application_id=application_id)
            for application_detail in application_details:
                type_name_id = application_detail.type_name_id
                all_applications_details[type_name_id] = all_applications_details.get(type_name_id,
                                                                                      0) + application_detail.number
            print("application_id:{},all_applications_details:{}".format(application_id, all_applications_details))

            all_assessment_details = {}
            for inline_form in formset.forms:
                if inline_form.has_changed():
                    if inline_form._meta.model == LocalAssessmentDetail:
                        flag = True
                        type_name_id = inline_form.instance.library_name.type_name_id
                        number = inline_form.instance.number
                        all_assessment_details[type_name_id] = all_assessment_details.get(type_name_id, 0) + number
                    if inline_form._meta.model == CenterAssessmentDetail:
                        flag = True
                        type_name_id = inline_form.instance.library_name.type_name_id
                        number = inline_form.instance.number
                        all_assessment_details[type_name_id] = all_assessment_details.get(type_name_id, 0) + number
            print("application_id:{},all_assessment_details:{}".format(application_id, all_assessment_details))
            if flag and all_assessment_details != all_applications_details:
                raise ValidationError({"error_dict": "研判数量和申请数量不符。"})

        super(ExWarehousingApplicationAdmin, self).save_formset(request, form, formset, change)

    def save_model(self, request, obj, form, change):
        user = request.user
        application_id = obj.id
        application_user = user.first_name
        action = ""
        print("obj_id:{}, status:{}, next_node:{}, user_id:{}".format(
            obj.id, obj.status, obj.next_node, user.id
        ))
        # 分管领导审批 —— 局长审批 —— 主管科室研判 —— 研判之后生成出库单 —— 中央库管理员出库
        if form.changed_data or obj.next_node == str(user.id) or obj.create_user == user:
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
            elif obj.next_node == str(request.user.id):
                if obj.status == "1":
                    user = User.objects.filter(groups__name__contains="局长").first()
                    if user:
                        obj.status = "2"
                        obj.next_node = user.id
                        action = "通过"
                elif obj.status == "2":
                    user = User.objects.filter(groups__name__contains="主管科室").first()
                    if user:
                        obj.status = "3"
                        obj.next_node = user.id
                        action = "通过"
                elif obj.status == "3":
                    user = User.objects.filter(groups__name__contains="仓库管理员").first()
                    if user:
                        obj.status = "4"
                        obj.next_node = user.id
                        action = "研判完成"
                # elif obj.status == "5":
                #     obj.status = "6"
                #     user = User.objects.filter(groups__name__contains="仓库管理员").first()
                #     if user:
                #         obj.next_node = user.id
                #         application_user = user.first_name,
                #         action = "通过"

            super(ExWarehousingApplicationAdmin, self).save_model(request, obj, form, change)
            print(application_id, application_user, action)
            ApplicationHistory.objects.create(
                application_id=obj.id,
                application_user=application_user,
                action=action
            )
            # 研判之后生成对应的出库单
            if obj.status == "4":
                # 1.生成中央库出库单
                center_assement_details = CenterAssessmentDetail.objects.filter(application_id=obj.id)
                if center_assement_details.exists():
                    # (1) 创建大的出库单子
                    center_outbound_order, err = CenterOutboundOrder.objects.get_or_create(
                        app_code_id=obj.id
                    )
                    center_outbound_order.title = obj.title
                    center_outbound_order.applicant = obj.applicant
                    center_outbound_order.applicant_user = obj.applicant_user
                    center_outbound_order.des = obj.des
                    center_outbound_order.add_time = obj.add_time
                    center_outbound_order.add_date = obj.add_date
                    center_outbound_order.save()
                    # (2) 生成出库小单子
                    for center_assement_detail in center_assement_details:
                        center_outbound_oerder_detail, err = CenterOutboundOrderDetail.objects.get_or_create(
                            app_code_id=center_outbound_order.id,
                            assessment_detail_id=center_assement_detail.id,
                        )
                        center_outbound_oerder_detail.number = center_assement_detail.number
                        center_outbound_oerder_detail.save()
                    # (3) 同步审批记录
                    application_historys = ApplicationHistory.objects.filter(application_id=obj.id)
                    for application_history in application_historys:
                        center_outbound_order_detail, err = CenterOutboundOrderHistory.objects.get_or_create(
                            application_id=center_outbound_order.id,
                            history_detail_id=application_history.id,
                        )
                        center_outbound_order_detail.action = application_history.action
                        center_outbound_order_detail.add_time = application_history.add_time
                        center_outbound_order_detail.application_user = application_history.application_user
                        center_outbound_order_detail.save()
                # 2.生成地方库出库单
                local_assement_details = LocalAssessmentDetail.objects.filter(application_id=obj.id)
                if local_assement_details.exists():
                    total_price = {}
                    for local_assement_detail in local_assement_details:
                        # (1) 创建大的地方库出库单子
                        local_outbound_order, err = LocalOutboundOrder.objects.get_or_create(
                            app_code_id=obj.id,
                            user_id=local_assement_detail.library_name.library_name.supplier_name.user.id,
                        )
                        local_outbound_order.title = obj.title
                        local_outbound_order.applicant = obj.applicant
                        local_outbound_order.applicant_user = obj.applicant_user
                        local_outbound_order.des = obj.des
                        local_outbound_order.add_time = obj.add_time
                        local_outbound_order.add_date = obj.add_date
                        local_outbound_order.save()

                        local_outbound_oerder_detail, err = LocalOutboundOrderDetail.objects.get_or_create(
                            app_code_id=local_outbound_order.id,
                            assessment_detail_id=local_assement_detail.id,
                        )
                        local_outbound_oerder_detail.number = local_assement_detail.number
                        price = local_assement_detail.number * local_assement_detail.library_name.unit_price
                        local_outbound_oerder_detail.total_price = price
                        # 供应商总金额
                        local_outbound_order.total_price = obj.total_price + price
                        local_outbound_oerder_detail.save()
                        local_outbound_order.save()

                        # (3) 同步审批记录
                        application_historys = ApplicationHistory.objects.filter(application_id=obj.id)
                        for application_history in application_historys:
                            local_outbound_order_history_detail, err = LocalOutboundOrderHistory.objects.get_or_create(
                                application_id=local_outbound_order.id,
                                history_detail_id=application_history.id,
                            )
                            local_outbound_order_history_detail.action = application_history.action
                            local_outbound_order_history_detail.application_user = application_history.application_user
                            local_outbound_order_history_detail.add_time = application_history.add_time
                            local_outbound_order_history_detail.save()

        super(ExWarehousingApplicationAdmin, self).save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        return super(ExWarehousingApplicationAdmin, self).response_add(request, obj, post_url_continue)

    def response_change(self, request, obj):
        return super(ExWarehousingApplicationAdmin, self).response_change(request, obj)

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        if object_id:
            extra_context = extra_context if extra_context else {}
            user = request.user
            obj = self.model.objects.get(id=object_id)
            print("changeform_view self:{}, object_id:{} user_id:{}, next_node:{}, status:{}".format(
                self, object_id, user.id, obj.next_node, obj.status)
            )
            if str(user.id) == obj.next_node:
                extra_context["can_approve"] = True
            else:
                extra_context["can_approve"] = False
        return super(ExWarehousingApplicationAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def get_inline_formsets(self, request, formsets, inline_instances, obj=None):
        return super(ExWarehousingApplicationAdmin, self).get_inline_formsets(request, formsets, inline_instances, obj)

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            print("get_formsets_with_inlines", inline, inline.get_formset(request, obj))
            yield inline.get_formset(request, obj), inline

    def has_change_permission(self, request, obj=None):
        user = request.user
        if obj:
            # print("has_change_permission obj:{}, next_node:{}. user_id:{}, opts:{}".format(
            #     obj, obj.next_node, user.id, self.opts
            # ))
            if obj.next_node == str(user.id) or obj.create_user == user:
                return True
            return False
        return super(ExWarehousingApplicationAdmin, self).has_change_permission(request, obj)


csrf_protect_m = method_decorator(csrf_protect)

from django.contrib.admin.views.main import ChangeList


class MyChangeList(ChangeList):

    def get_results(self, *args, **kwargs):
        super(MyChangeList, self).get_results(*args, **kwargs)
        # print("result_list:{},type:{}".format(self.result_list, type(self.result_list)))
        # ret = self.result_list
        # q = self.result_list.aggregate(put_number_sum=Sum('number'))
        # # q2 = self.result_list.filter(action="2").aggregate(push_number_sum=Sum('number'))
        #
        # print(q['put_number_sum'])
        # self.put_number_sum = q['put_number_sum']
        # self.push_number_sum = q2['push_number_sum']

    def get_queryset(self, request):
        return super(MyChangeList, self).get_queryset(request)


@admin.register(Accounts)
class AccountsaAdmin(admin.ModelAdmin):
    list_filter = ["db_type", "action", "type_name"]
    date_hierarchy = "add_date"
    list_display = ["app_code", "db_type", "entry_name", "action", "type_name", "specifications", "unit", "number",
                    "price",
                    "unit_price", "add_date"]
    change_list_template = "material_application/accounts_change_list.html"

    actions = ['download_accounts']
    list_per_page = 50

    def download_accounts(self, request, queryset):
        records = list(queryset.values())
        #  数据库的英文字段和中文字段的映射字典
        zh_en = {
            '物料名称': 'materials_name',
            '规格': 'specifications',
            '单位': 'unit',
        }
        zh = list(zh_en.keys())
        zh.extend(["单价(元)"])
        #  转换数据格式，以方便openpyxl批量写入
        records_list = [zh]
        print()
        for r in records:
            print(r)
        #  开始批量写入数据
        wb = Workbook()
        ws = wb.active
        for row in records_list:
            ws.append(row)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename="台账记录.xlsx"'
        wb.save(response)
        return response

    download_accounts.short_description = u'导出台账'

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context if extra_context else {}
        response = super().changelist_view(request, extra_context)
        # print(hasattr(response, "context_data"))
        if hasattr(response, "context_data") and "cl" in response.context_data:
            cl = response.context_data["cl"]
            filtered_query_set = cl.get_queryset(request)
            put_number_sum = 0
            push_number_sum = 0
            for i in filtered_query_set:
                if i.action == "1":
                    put_number_sum += i.number
                else:
                    push_number_sum += i.number
            response.context_data["put_number_sum"] = put_number_sum
            response.context_data["push_number_sum"] = push_number_sum
        return response

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
