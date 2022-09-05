import logging
import traceback

from django.contrib import admin
from django.utils.html import format_html
from home.models import CodeNumber, MaterialsType
from material_application.models import Accounts

from utils.utils import parse_center_excel_data
from .models import *

logger = logging.getLogger("django")


# 中央库基本信息
@admin.register(CenterLibrary)
class CenterLibraryAdmin(admin.ModelAdmin):
    list_display = ["library_name", "total_budget", "add_date", "create_user"]
    fields = ["library_name", "total_budget", "des"]
    save_as_continue = False
    save_as = False
    date_hierarchy = "add_date"

    def save_model(self, request, obj, form, change):
        obj.create_user = request.user
        super(CenterLibraryAdmin, self).save_model(request, obj, form, change)


# 物料详情
class MaterialsDetailInline(admin.TabularInline):
    model = CenterLabraryMaterials
    extra = 0
    fields = ["type_name", "put_num", "unit_price", "total_price"]
    autocomplete_fields = ["type_name"]


# 申请文件
class CenterWarehousingFileInline(admin.TabularInline):
    model = CenterWarehousingFile
    extra = 0
    fields = ["file"]


# 入库单
@admin.register(CenterWarehousingApplication)
class CenterWarehousingApplicationAdmin(admin.ModelAdmin):
    list_display = ["app_code", "total_price", "create_u", "add_date"]
    search_fields = ["app_code", "create_u"]
    date_hierarchy = "add_time"
    inlines = [CenterWarehousingFileInline, MaterialsDetailInline]
    save_as_continue = False
    save_as = False
    db_name = "CenterWarehousingApplication"
    readonly_fields = []
    fields = [("total_price", "file"), "des", "add_time"]

    def save_formset(self, request, form, formset, change):
        all_total_price = 0
        for inline_form in formset.forms:
            if inline_form._meta.model == CenterLabraryMaterials and inline_form.has_changed():
                type_name = inline_form.instance.type_name
                put_num = inline_form.instance.put_num
                unit_price = inline_form.instance.unit_price
                total_price = unit_price * put_num
                inline_form.instance.total_price = total_price
                datas = CenterLabraryQuantity.objects.filter(type_name=type_name)
                # 计算该物资总数量
                if datas.exists():
                    data = datas[0]
                    data.put_num = data.put_num + put_num
                    data.balance_num = data.balance_num + put_num
                    data.total_price = total_price
                    data.save()
                else:
                    CenterLabraryQuantity.objects.create(
                        type_name=type_name,
                        put_num=put_num,
                        unit_price=unit_price,
                        balance_num=put_num,
                        total_price=total_price
                    )
                # 入库增加台账记录
                Accounts.save_one(
                    inline_form.instance.ware_app.app_code,
                    "",
                    "",
                    inline_form.instance.type_name.materials_name,
                    inline_form.instance.type_name.specifications,
                    inline_form.instance.type_name.unit,
                    "1",
                    unit_price,
                    put_num,
                    total_price,
                    "2"
                )
                all_total_price += total_price

        # 转换为万元
        form.instance.total_price = all_total_price / 10000
        form.instance.save()
        super().save_formset(request, form, formset, change)

    def save_model(self, request, obj, form, change):
        # 创建时生成单号
        if not obj.app_code:
            obj.create_u = request.user
            obj.app_code = CodeNumber.get_app_code(self.db_name)
        super().save_model(request, obj, form, change)

        # 解析上传的文件
        logger.info("file_path:{}".format(obj.file))
        if obj.file:
            file_path = obj.file.path
            # 解析上传的附件
            for row_data in parse_center_excel_data(file_path):
                try:
                    materials_type, err = MaterialsType.objects.get_or_create(
                        materials_name=row_data[0],
                        unit=row_data[1],
                        specifications=row_data[2],
                    )
                    center_labrary_materials, err = CenterLabraryMaterials.objects.get_or_create(
                        ware_app_id=obj.id,
                        type_name_id=materials_type.id,
                    )
                    unit_price = row_data[3]
                    put_num = row_data[4]
                    total_price = float(unit_price) * float(put_num)
                    center_labrary_materials.unit_price = row_data[3]
                    center_labrary_materials.put_num = row_data[4]
                    center_labrary_materials.total_price = total_price
                    center_labrary_materials.add_time = timezone.now()
                    center_labrary_materials.add_date = timezone.now()
                    center_labrary_materials.modify_time = timezone.now()
                    center_labrary_materials.save()
                    # 增加台账记录
                    Accounts.save_one(
                        obj.app_code,
                        "",
                        "",
                        materials_type.materials_name,
                        materials_type.specifications,
                        materials_type.type_name.unit,
                        "1",
                        unit_price,
                        row_data[3],
                        total_price,
                        "2"
                    )
                except:
                    logger.error("save data error:{}, error:{}".format(row_data, traceback.format_exc()))

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.readonly_fields = ["app_code", "create_u"]
        return self.readonly_fields

    def get_fields(self, request, obj=None):
        if obj:
            self.fields = [("app_code", "create_u"), ("total_price", "file"), "des", "add_time"]
        return self.fields

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# 物资总库存
@admin.register(CenterLabraryQuantity)
class CenterLabraryQuantityAdmin(admin.ModelAdmin):
    list_display = ["type_name", "put_num", "push_num", "colored_balance_num", "unit_price", "total_price", "out_price"]
    list_filter = [
        "type_name__materials_name",
    ]
    search_fields = ["type_name__materials_name", "balance_num"]

    def colored_balance_num(self, obj):
        mater_type = MaterialsType.objects.filter(materials_name=obj.type_name)
        if mater_type.exists():
            ratio = mater_type[0].warning_quantity

        else:
            ratio = 10
        if obj.balance_num <= obj.put_num * ratio / 100:
            color_code = 'red'
            msg = "(库存预警)"
        else:
            color_code = 'green'
            msg = ""
        return format_html(
            '<span style="color:{};">{}</span>', color_code, str(obj.balance_num) + msg,
        )

    colored_balance_num.short_description = u'结余数量'

    def get_search_results(self, request, queryset, search_term):
        searchs = search_term.split('-')
        number1 = None
        number2 = None
        try:
            if len(searchs) >= 2:
                number1 = int(searchs[0])
                number2 = int(searchs[1])
                search_term = ''
        except ValueError:
            pass
        queryset, use_distinct = super(CenterLabraryQuantityAdmin, self).get_search_results(
            request, queryset, search_term
        )
        if number1 and number2:
            queryset = self.model.objects.filter(balance_num__gte=number1, balance_num__lte=number2)
        return queryset, use_distinct

    def save_model(self, request, obj, form, change):
        put_num = obj.put_num
        push_num = obj.push_num
        unit_price = obj.unit_price
        obj.balance_num = put_num - push_num
        obj.total_price = put_num * unit_price
        super().save_formset(request, form, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class CenterOutboundOrderDetailInline(admin.TabularInline):
    fields = ["assessment_detail", "number", "total_price"]
    model = CenterOutboundOrderDetail

    def has_change_permission(self, request, obj=None):
        return None

    def has_delete_permission(self, request, obj=None):
        return None

    def has_add_permission(self, request, obj):
        return None


class CenterOutboundOrderHistoryInline(admin.TabularInline):
    fields = ["application_user", "action", "add_time"]
    model = CenterOutboundOrderHistory

    def has_change_permission(self, request, obj=None):
        return None

    def has_delete_permission(self, request, obj=None):
        return None

    def has_add_permission(self, request, obj):
        return None


# 中央库出库单
@admin.register(CenterOutboundOrder)
class CenterOutboundOrderAdmin(admin.ModelAdmin):
    list_display = ["app_code", "title", "applicant", "is_ex", "is_check", "html_short", "pdf_short"]
    inlines = [CenterOutboundOrderDetailInline]
    readonly_fields = ["app_code", "title", "applicant", "applicant_user",
                       "des", "total_price", "add_date", "add_time"]
    fieldsets = [
        ("基本信息", {"fields": (("app_code", "total_price"),)}),
        ("申请信息", {"fields": (("applicant", "applicant_user"), "title", "des", "add_date", "is_ex", "is_check")}),
    ]

    def html_short(self, obj):
        return format_html(
            '<a href="{}?object_id={}" target="_blank">{}</a>'.format("/material_application/center_order_html/",
                                                                      obj.id, "点击查看", )
        )

    html_short.short_description = u'查看电子单'

    def pdf_short(self, obj):
        return format_html(
            '<a href="{}?object_id={}&db_type={}">{}</a>'.format(
                "/material_application/download_order_pdf/", obj.id, "center", "点击下载"
            )
        )

    pdf_short.short_description = u'电子单下载'

    def has_change_permission(self, request, obj=None):
        # 核销之后不允许修改
        if obj and obj.is_check:
            return None
        ret = super().has_change_permission(request, obj)
        logger.info("has_change_permission:{}".format(ret))
        return ret

    def has_delete_permission(self, request, obj=None):
        return None

    def has_add_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change and obj and obj.is_check:
            order_details = CenterOutboundOrderDetail.objects.filter(app_code_id=obj.id)
            for order_detail in order_details:
                app_code = order_detail.app_code.app_code.app_code
                type_name = order_detail.assessment_detail.library_name.type_name.materials_name
                specifications = order_detail.assessment_detail.library_name.type_name.specifications
                unit = order_detail.assessment_detail.library_name.type_name.unit
                unit_price = order_detail.assessment_detail.library_name.unit_price
                number = order_detail.number
                price = order_detail.total_price
                # 申请单位
                applicant = obj.applicant
                action = "2"
                logger.info(
                    "app_code:{},type_name:{},specifications:{},unit:{},unit_price:{},number:{},price:{}".format(
                        app_code, type_name, specifications, unit, unit_price, number, price,
                    ))
                # 出库记录+1
                Accounts.save_one(
                    app_code,
                    "",
                    "",
                    type_name,
                    specifications,
                    unit,
                    action,
                    unit_price,
                    number=number,
                    price=price,
                    db_type="2",
                    applicant=applicant
                )
                # 该商品的出库数量+number
                center_labrary_quantity = CenterLabraryQuantity.objects.filter(
                    id=order_detail.assessment_detail.library_name_id).first()

                # 修改物料库存的出库数量、出库金额
                if center_labrary_quantity:
                    push_num = center_labrary_quantity.push_num
                    center_labrary_quantity.push_num = push_num + number
                    center_labrary_quantity.out_price = center_labrary_quantity.out_price + price
                    center_labrary_quantity.balance_num = center_labrary_quantity.put_num - center_labrary_quantity.push_num
                    center_labrary_quantity.save()

    def get_readonly_fields(self, request, obj=None):
        user = request.user

        warehouse_manage = user.groups.filter(name="仓库管理员").first()
        suplier_manage = user.groups.filter(name="供应商").first()

        # 没有出库权限，则修改出库为只读
        if not warehouse_manage and "is_ex" not in self.readonly_fields:
            self.readonly_fields.append("is_ex")
        elif warehouse_manage and "is_ex" in self.readonly_fields:
            self.readonly_fields.remove("is_ex")
        # 没有核销权限，则修改核销为只读
        if not warehouse_manage and "is_check" not in self.readonly_fields:
            self.readonly_fields.append("is_check")
        elif warehouse_manage and "is_check" in self.readonly_fields:
            self.readonly_fields.remove("is_check")
        logger.info("仓库管理员:{}, 供应商:{}, readonly_fields:{}".format(
            warehouse_manage, suplier_manage, self.readonly_fields)
        )
        return self.readonly_fields
