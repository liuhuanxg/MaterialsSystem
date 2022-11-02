import logging

from django.contrib import admin
from django.utils.html import format_html
from home.models import CodeNumber, MaterialsType
from material_application.models import Accounts

from utils.utils import parse_excel_data
from .models import *

logger = logging.getLogger("django")


class LocalWarehousingFileInline(admin.TabularInline):
    model = LocalWarehousingFile
    extra = 0


# 物料详情
@admin.register(LocalLabraryMaterials)
class LocalLabraryMaterialsAdmin(admin.ModelAdmin):
    list_display = ["library_name", "type_name", "push_num", "supplier_name", "push_total_price", "add_date",
                    "library_name__is_approve"]
    list_filter = ["library_name__entry_name", "type_name__materials_name"]
    search_fields = ["library_name__entry_name", "type_name__materials_name", "type_name__specifications",
                     "type_name__unit"]
    date_hierarchy = "add_date"
    readonly_fields = ["library_name", "type_name", "push_num", "unit_price", "add_time"]

    def supplier_name(self, obj):
        return obj.library_name.supplier_name

    supplier_name.short_description = u'供应商'

    def push_total_price(self, obj):
        return str(obj.unit_price * obj.push_num)

    push_total_price.short_description = u'出库金额(元)'

    def library_name__is_approve(self, obj):
        if obj.library_name.is_approve:
            msg = "是"
            color_code = "green"
        else:
            msg = "否"
            color_code = "red"
        return format_html(
            '<span style="color:{};">{}</span>', color_code, str(msg),
        )

    library_name__is_approve.short_description = u'是否审核'

    def save_model(self, request, obj, form, change):
        super().save_model(request, form, form, change)

    def save_formset(self, request, form, formset, change):
        super().save_formset(request, form, formset, change)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        user = request.user
        if user.groups.filter(name="地方库供应商").exists():
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        return False

    # 供应商只能看到自己的数据
    def get_queryset(self, request):
        qs = super(LocalLabraryMaterialsAdmin, self).get_queryset(request)
        user = request.user
        if user.groups.filter(name="地方库供应商").exists():
            supplier_messages = SupplierMessage.objects.filter(user_id=user.id)
            if supplier_messages.exists():
                supplier_messages = supplier_messages[0]
                qs = qs.filter(library_name__supplier_name=supplier_messages.id)
        return qs


# 物料详情inline
class MaterialsDetailInline(admin.TabularInline):
    model = LocalLabraryMaterials
    extra = 0
    fields = ["type_name", "unit_price"]
    exclude = ["id"]
    readonly_fields = ["id"]
    autocomplete_fields = ["type_name"]


# 入库单申请
@admin.register(LocalLibrary)
class LocalLibraryAdmin(admin.ModelAdmin):
    list_display = ["app_code", "entry_name", "supplier_name", "budget", "less_budget_status", "is_approve", "add_date"]
    search_fields = ["app_code", "create_user"]
    list_filter = ["is_approve"]
    date_hierarchy = "add_time"
    inlines = [LocalWarehousingFileInline, MaterialsDetailInline]
    db_name = "LocalWarehousingApplication"
    readonly_fields = ["app_code", "create_user", "less_budget"]
    fields = [("entry_name", "supplier_name"), ("budget", "less_budget"), ("add_date", "file"), "des"]

    def less_budget_status(self, obj):
        if obj.less_budget <= obj.budget * 0.1:
            msg = obj.less_budget
            color_code = "red"
        else:
            msg = obj.less_budget
            color_code = "green"
        return format_html(
            '<span style="color:{};">{}</span>', color_code, str(msg),
        )

    less_budget_status.short_description = u'剩余预算'

    def get_fields(self, request, obj=None):
        fields = self.fields
        is_approve = "is_approve"
        if not obj:
            if request.user.has_perm('can_approve') and is_approve not in fields:
                fields.append(is_approve)
        elif obj and not obj.is_approve and is_approve not in fields:
            fields.append(is_approve)
        return fields

    def has_change_permission(self, request, obj=None):
        user = request.user
        if obj and obj.is_approve:
            # if user.groups.filter(name="地方库供应商"):
            #     return False
            # else:
            #     return True
            return False
        if obj:
            if not request.user.has_perm('can_approve') and "is_approve" not in self.readonly_fields:
                self.readonly_fields.append("is_approve")
            elif request.user.has_perm('can_approve') and "is_approve" in self.readonly_fields:
                self.readonly_fields.remove("is_approve")

        self.readonly_fields = list(set(self.readonly_fields))
        return super(LocalLibraryAdmin, self).has_change_permission(request, obj)

    def save_model(self, request, obj, form, change):
        if not obj.app_code:
            obj.create_user = request.user
            obj.app_code = CodeNumber.get_app_code(self.db_name)
        super(LocalLibraryAdmin, self).save_model(request, obj, form, change)
        is_approve = obj.is_approve
        logger.info("obj.file:{}".format(obj.file))
        if obj.file:
            file_path = obj.file.path
            # 解析上传的附件
            for row_data in parse_excel_data(file_path):
                materials_type, err = MaterialsType.objects.get_or_create(
                    materials_name=row_data[0],
                    unit=row_data[1],
                    specifications=row_data[2],
                )
                local_labrary_materials, err = LocalLabraryMaterials.objects.get_or_create(
                    library_name_id=obj.id,
                    type_name_id=materials_type.id,
                )
                local_labrary_materials.unit_price = row_data[3]
                local_labrary_materials.add_time = timezone.now()
                local_labrary_materials.add_date = timezone.now()
                local_labrary_materials.modify_time = timezone.now()
                local_labrary_materials.save()

        if is_approve:
            # 第一次审核通过之后同步剩余预算金额
            obj.less_budget = obj.budget
            local_labrary_materials = LocalLabraryMaterials.objects.filter(library_name_id=obj.id)
            # 审核之后同步台账记录
            for inline_form in local_labrary_materials:
                type_name = inline_form.type_name.materials_name
                specifications = inline_form.type_name.specifications
                unit = inline_form.type_name.unit
                app_code = obj.app_code
                unit_price = inline_form.unit_price
                print(type_name, unit_price)
                # 入库，增加台账记录
                Accounts.save_one(
                    app_code,
                    obj.supplier_name.company_name,
                    obj.entry_name,
                    type_name,
                    specifications,
                    unit,
                    "1",
                    unit_price,
                    0,
                    0
                )
        super(LocalLibraryAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        super().save_formset(request, form, formset, change)

    # 获取只读字段
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = self.readonly_fields
        if not obj:
            if not request.user.has_perm('can_approve'):
                readonly_fields.append("is_approve")
        elif obj and obj.is_approve:
            readonly_fields = ["app_code", "entry_name", "library_name", "create_user"]
        return readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        return super(LocalLibraryAdmin, self).add_view(request, form_url, extra_context)

    # 供应商只能看到自己的数据
    def get_queryset(self, request):
        qs = super(LocalLibraryAdmin, self).get_queryset(request)
        user = request.user
        supplier_messages = SupplierMessage.objects.filter(user_id=user.id)
        if supplier_messages.exists():
            supplier_messages = supplier_messages[0]
            qs = qs.filter(supplier_name_id=supplier_messages.id)
        return qs

    # 不能选择其他供应商
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        user = request.user
        logger.info('request.user.has_perm_can_approve:{}'.format(user.has_perm("can_approve")))
        supplier_messages = SupplierMessage.objects.filter(user_id=user.id)
        if supplier_messages and db_field.name == "supplier_name":
            kwargs["queryset"] = supplier_messages
            kwargs['initial'] = supplier_messages.first()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        return super(LocalLibraryAdmin, self).change_view(request, object_id, form_url, extra_context)

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        if not object_id:
            local_library = LocalLibrary.objects.filter(id=object_id)
            if local_library.exists():
                local_library = local_library[0]
                if local_library.is_approve:
                    self.readonly_fields = ["app_code", "entry_name", "supplier_name", "add_time"]
        return super(LocalLibraryAdmin, self).changeform_view(request, object_id, form_url, extra_context)

    def get_inline_formsets(self, request, formsets, inline_instances, obj=None):
        return super(LocalLibraryAdmin, self).get_inline_formsets(request, formsets, inline_instances, obj)


class SupplierFileInline(admin.TabularInline):
    model = SupplierFile
    extra = 0


# 供应商信息
@admin.register(SupplierMessage)
class SupplierMessageAdmin(admin.ModelAdmin):
    list_display = ["company_name", "add_time", "modify_time"]
    inlines = [SupplierFileInline]

    # 只能看到自己的数据
    def get_queryset(self, request):
        user = request.user
        qs = super(SupplierMessageAdmin, self).get_queryset(request)
        if not user.groups.filter(name__contains="地方库供应商"):
            return qs

        return qs.filter(user=request.user.id)


# 出库单详情
class LocalOutboundOrderDetailInline(admin.TabularInline):
    model = LocalOutboundOrderDetail
    extra = 0
    fields = ["assessment_detail", "number", "total_price"]

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# 出库单
@admin.register(LocalOutboundOrder)
class LocalOutboundOrderAdmin(admin.ModelAdmin):
    list_display = ["app_code", "user", "title", "applicant", "is_ex", "is_check", "html_short", "pdf_short"]
    readonly_fields = ["app_code", "user", "title", "applicant", "applicant_user",
                       "des", "total_price", "add_date", "add_time", "applicant_phone"
                       ]

    fieldsets = [
        ("基本信息", {"fields": (("app_code", "user", "total_price"),)}),
        ("申请信息", {"fields": (("applicant", "applicant_user", "applicant_phone"), "title", "des", "add_date", "is_ex", "is_check")}),
    ]

    def html_short(self, obj):
        return format_html(
            '<a href="{}?object_id={}" target="_blank">{}</a>'.format(
                "/material_application/local_order_html/", obj.id, "点击查看"
            )
        )

    html_short.short_description = u'查看电子单'

    def pdf_short(self, obj):
        return format_html(
            '<a href="{}?object_id={}&db_type={}">{}</a>'.format(
                "/material_application/download_order_pdf/", obj.id, "local", "点击下载"
            )
        )

    pdf_short.short_description = u'电子单下载'
    inlines = [LocalOutboundOrderDetailInline]

    # 供应商只能看到自己的出库单
    def get_queryset(self, request):
        user = request.user
        qs = super(LocalOutboundOrderAdmin, self).get_queryset(request)
        if user.groups.filter(name="地方库供应商").exists():
            qs = qs.filter(user_id=user.id)
        return qs

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        # 出库之后不允许再修改
        if obj and obj.is_check:
            return None
        return super(LocalOutboundOrderAdmin, self).has_change_permission(request, obj)

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        response = super(LocalOutboundOrderAdmin, self).changeform_view(request, object_id, form_url, extra_context)
        return response

    def save_model(self, request, obj, form, change):
        super(LocalOutboundOrderAdmin, self).save_model(request, obj, form, change)

        if change and obj and obj.is_check:
            order_details = LocalOutboundOrderDetail.objects.filter(app_code_id=obj.id)
            for order_detail in order_details:
                app_code = order_detail.app_code.app_code.app_code
                # 出库选择的供应商名称
                supplier_name = order_detail.assessment_detail.library_name.library_name.supplier_name.company_name
                type_name = order_detail.assessment_detail.library_name.type_name.materials_name
                specifications = order_detail.assessment_detail.library_name.type_name.specifications
                unit = order_detail.assessment_detail.library_name.type_name.unit
                unit_price = order_detail.assessment_detail.library_name.unit_price
                number = order_detail.number
                price = order_detail.total_price
                applicant = obj.applicant
                action = "2"
                print("app_code:{},type_name:{},specifications:{},unit:{},unit_price:{},number:{},price:{}".format(
                    app_code, type_name, specifications, unit, unit_price, number, price,
                ))
                # 出库记录+1
                Accounts.save_one(
                    app_code,
                    supplier_name,
                    "",
                    type_name,
                    specifications,
                    unit,
                    action,
                    unit_price,
                    number=number,
                    price=price,
                    db_type="1",
                    applicant=applicant
                )
                # 该商品的出库数量+number
                local_labrary_material = LocalLabraryMaterials.objects.filter(
                    id=order_detail.assessment_detail.library_name_id).first()

                # 修改物料库存的出库数量
                if local_labrary_material:
                    push_num = local_labrary_material.push_num
                    local_labrary_material.push_num = push_num + number
                    local_labrary_material.save()
                local_library = LocalLibrary.objects.filter(
                    id=order_detail.assessment_detail.library_name.library_name_id).first()

                # 修改地方库的剩余预算
                if local_library:
                    less_budget = local_library.less_budget
                    local_library.less_budget = (less_budget * 10000 - price) / 10000
                    local_library.save()

    def get_readonly_fields(self, request, obj=None):
        user = request.user

        warehouse_manage = user.groups.filter(name="仓库管理员").first()
        suplier_manage = user.groups.filter(name="地方库供应商").first()

        # 没有出库权限，则修改出库为只读
        if not warehouse_manage and "is_ex" not in self.readonly_fields:
            self.readonly_fields.append("is_ex")
        elif warehouse_manage and "is_ex" in self.readonly_fields:
            self.readonly_fields.remove("is_ex")
        # 没有核销权限，则修改核销为只读
        if not suplier_manage and "is_check" not in self.readonly_fields:
            self.readonly_fields.append("is_check")
        elif suplier_manage and "is_check" in self.readonly_fields:
            self.readonly_fields.remove("is_check")
        logger.info("仓库管理员:{}, 供应商:{}, readonly_fields:{}".format(
            warehouse_manage, suplier_manage, self.readonly_fields)
        )
        return self.readonly_fields
