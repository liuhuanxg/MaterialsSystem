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
    list_display = ["library_name", "type_name", "push_num", "colored_balance_quantity",
                    "add_time"]
    list_filter = ["library_name__library_name", "type_name__materials_name"]
    search_fields = ["library_name__library_name", "balance_quantity"]
    date_hierarchy = "add_date"
    readonly_fields = ["library_name", "type_name", "push_num", "colored_balance_quantity",
                       "add_time"]

    def colored_balance_quantity(self, obj):
        if obj.balance_quantity <= 10:
            color_code = 'red'
        else:
            color_code = 'green'
        return format_html(
            '<span style="color:{};">{}</span>', color_code, str(obj.balance_quantity) + "(库存预警)",
        )

    colored_balance_quantity.short_description = u'结余数量'

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
        queryset, use_distinct = super(LocalLabraryMaterialsAdmin, self).get_search_results(request, queryset,
                                                                                            search_term)
        if number1 and number2:
            queryset = self.model.objects.filter(balance_quantity__gte=number1, balance_quantity__lte=number2)
        return queryset, use_distinct

    def save_model(self, request, obj, form, change):
        super().save_model(request, form, form, change)

    def save_formset(self, request, form, formset, change):
        super().save_formset(request, form, formset, change)


class MaterialsDetailInline(admin.TabularInline):
    model = LocalLabraryMaterials
    extra = 0
    fields = ["type_name", "unit_price"]


# 入库单申请
@admin.register(LocalLibrary)
class LocalLibraryAdmin(admin.ModelAdmin):
    list_display = ["app_code", "entry_name", "library_name", "create_user", "is_approve", "add_time", "add_date",
                    "modify_time"]
    search_fields = ["app_code", "create_user"]
    date_hierarchy = "add_time"
    inlines = [LocalWarehousingFileInline, MaterialsDetailInline]
    save_as_continue = False
    save_as = False
    db_name = "LocalWarehousingApplication"
    readonly_fields = ["app_code", "create_user"]

    def save_model(self, request, obj, form, change):
        date_str = get_date_str()
        code_number = CodeNumber.objects.filter(date_str=date_str, db_name=self.db_name).first()
        if code_number:
            number = code_number.number + 1
            code_number.number = number
            code_number.save()
        else:
            number = 1
            CodeNumber.objects.create(date_str=date_str, db_name=self.db_name, number=number)
        obj.create_user = request.user
        obj.app_code = CodeNumber.get_app_code(self.db_name)
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
        readonly_fields = ["create_user"]
        if not obj:
            if not request.user.has_perm('can_approve'):
                readonly_fields.append("is_approve")
        elif obj and obj.is_approve:
            readonly_fields = ["app_code", "entry_name", "library_name", "create_user", "is_approve"]

        return readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        return super(LocalLibraryAdmin, self).add_view(request, form_url, extra_context)

    # 只能看到自己的数据
    def get_queryset(self, request):
        qs = super(LocalLibraryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(create_user=request.user.id)


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
