import traceback

import xlrd
from django.contrib import admin
from django.utils.html import format_html
from home.models import CodeNumber

from utils.date_utils import get_date_str
from .models import *


class LocalWarehousingFileInline(admin.TabularInline):
    model = LocalWarehousingFile
    extra = 1


@admin.register(LocalLabraryMaterials)
class LocalLabraryMaterialsAdmin(admin.ModelAdmin):
    list_display = ["library_name", "type_name", "push_num", "push_total_price", "add_date", "library_name__is_approve"]
    list_filter = ["library_name__entry_name", "type_name__materials_name"]
    search_fields = ["library_name__entry_name", "balance_quantity"]
    date_hierarchy = "add_date"
    readonly_fields = ["library_name", "type_name", "push_num", "unit_price", "add_time"]

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
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # 供应商只能看到自己的数据
    def get_queryset(self, request):
        qs = super(LocalLabraryMaterialsAdmin, self).get_queryset(request)
        supplier_messages = SupplierMessage.objects.filter(user_id=request.user.id)
        if supplier_messages.exists():
            supplier_messages = supplier_messages[0]
            qs.filter(library_name__supplier_name=supplier_messages.id)
        return qs


class MaterialsDetailInline(admin.TabularInline):
    model = LocalLabraryMaterials
    extra = 0
    fields = ["type_name", "unit_price"]
    exclude = ["id"]
    readonly_fields = ["id"]


# 入库单申请
@admin.register(LocalLibrary)
class LocalLibraryAdmin(admin.ModelAdmin):
    list_display = ["app_code", "entry_name", "supplier_name", "budget", "less_budget", "is_approve", "add_date"]
    search_fields = ["app_code", "create_user"]
    list_filter = ["is_approve"]
    date_hierarchy = "add_time"
    inlines = [LocalWarehousingFileInline, MaterialsDetailInline]
    db_name = "LocalWarehousingApplication"
    readonly_fields = ["app_code", "create_user", "less_budget"]

    fields = (("entry_name", "supplier_name", "budget"), ("file", "add_date"))

    def get_fields(self, request, obj=None):
        fields = [("entry_name", "supplier_name"), ("file", "add_date")]
        if not obj:
            if request.user.has_perm('can_approve'):
                fields.append(("is_approve"), )
        elif obj and not obj.is_approve:
            fields.append(("is_approve"), )

        return fields

    def save_model(self, request, obj, form, change):
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
        file_path = obj.file.path
        if file_path:
            ret = parse_excel_data(file_path)
        super(LocalLibraryAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        super().save_formset(request, form, formset, change)

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(LocalLibraryAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'app_code':
            field.initial = CodeNumber.get_app_code(db_name=self.db_name)
        return field

    # 获取只读字段
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = self.readonly_fields
        if not obj:
            if not request.user.has_perm('can_approve'):
                readonly_fields.append("is_approve")
        elif obj and obj.is_approve:
            readonly_fields = ["app_code", "entry_name", "library_name", "create_user", "is_approve"]

        return readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        return super(LocalLibraryAdmin, self).add_view(request, form_url, extra_context)

    # 供应商只能看到自己的数据
    def get_queryset(self, request):
        qs = super(LocalLibraryAdmin, self).get_queryset(request)
        supplier_messages = SupplierMessage.objects.filter(user_id=request.user.id)
        if supplier_messages.exists():
            supplier_messages = supplier_messages[0]
            qs.filter(supplier_name_id=supplier_messages.id)
        return qs

    # 不能选择其他供应商
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.has_perm("can_approve") and db_field.name == "supplier_name":
            supplier_messages = SupplierMessage.objects.filter(user_id=request.user.id)
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
                    self.readonly_fields = ["app_code", "entry_name", "supplier_name", "is_approve", "add_time"]
        return super(LocalLibraryAdmin, self).changeform_view(request, object_id, form_url, extra_context)


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
        qs = super(SupplierMessageAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user.id)


def parse_excel_data(file_path):
    try:

        wb = xlrd.open_workbook(file_path)
        # 获取并打印 sheet 数量
        print("sheet 数量:", wb.nsheets)
        # 获取并打印 sheet 名称
        print("sheet 名称:", wb.sheet_names())
        # 根据 sheet 索引获取内容
        sh1 = wb.sheet_by_index(0)
        # 也可根据 sheet 名称获取内容
        # sh = wb.sheet_by_name('成绩')
        # 获取并打印该 sheet 行数和列数
        print(u"sheet %s 共 %d 行 %d 列" % (sh1.name, sh1.nrows, sh1.ncols))
        # 获取并打印某个单元格的值
        print("第一行第二列的值为:", sh1.cell_value(0, 1))
        # 获取整行或整列的值
        rows = sh1.row_values(0)  # 获取第一行内容
        cols = sh1.col_values(1)  # 获取第二列内容
        # 打印获取的行列值
        print("第一行的值为:", rows)
        print("第二列的值为:", cols)
        # 获取单元格内容的数据类型
        print("第二行第一列的值类型为:", sh1.cell(1, 0).ctype)
    except:
        print("parse_excel_data error:{}".format(traceback.format_exc()))
