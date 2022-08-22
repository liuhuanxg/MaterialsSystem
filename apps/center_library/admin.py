from django.contrib import admin
from django.utils.html import format_html
from home.models import CodeNumber, MaterialsType

from utils.date_utils import get_date_str
from .models import *


# 中央库基本信息
@admin.register(CenterLibrary)
class CenterLibraryAdmin(admin.ModelAdmin):
    list_display = ["library_name", "add_time", "create_user", "total_budget"]
    fields = ["library_name", "total_budget", "des"]
    save_as_continue = False
    save_as = False

    def save_model(self, request, obj, form, change):
        obj.create_user = request.user
        super(CenterLibraryAdmin, self).save_model(request, obj, form, change)


# 物料详情
class MaterialsDetailInline(admin.TabularInline):
    model = CenterLabraryMaterials
    extra = 0
    fields = ["type_name", "put_num", "unit_price", "total_price"]


# 申请文件
class CenterWarehousingFileInline(admin.TabularInline):
    model = CenterWarehousingFile
    extra = 0
    fields = ["file"]


# 入库单申请
@admin.register(CenterWarehousingApplication)
class CenterWarehousingApplication(admin.ModelAdmin):
    list_display = ["app_code", "total_price", "create_u", "add_time", "add_date", "modify_time"]
    search_fields = ["app_code", "create_u"]
    date_hierarchy = "add_time"
    inlines = [CenterWarehousingFileInline, MaterialsDetailInline]
    save_as_continue = False
    save_as = False
    db_name = "CenterWarehousingApplication"
    readonly_fields = ["app_code", "create_u"]

    def save_formset(self, request, form, formset, change):
        for inline_form in formset.forms:
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
                data.total_price = total_price
                data.save()
            else:
                CenterLabraryQuantity.objects.create(
                    type_name=type_name,
                    put_num=put_num,
                    total_price=total_price
                )
        super().save_formset(request, form, formset, change)

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
        super(CenterWarehousingApplication, self).save_model(request, obj, form, change)


# 物资总库存
@admin.register(CenterLabraryQuantity)
class CenterLabraryQuantityAdmin(admin.ModelAdmin):
    list_display = ["type_name", "put_num", "push_num", "colored_balance_quantity", "total_price"]
    list_filter = ["type_name__materials_name"]
    search_fields = ["balance_quantity"]
    fields = []

    def colored_balance_quantity(self, obj):
        mater_type = MaterialsType.objects.filter(type_name=obj.type_name)
        if mater_type.exists():
            ratio = mater_type[0].warning_quantity

        else:
            ratio = 10
        if obj.balance_quantity <= obj.put_num * ratio / 100:
            color_code = 'red'
        else:
            color_code = 'green'
        return format_html(
            '<span style="color:{};">{}</span>', color_code, str(obj.balance_quantity) + "(库存预警)",
        )

    colored_balance_quantity.short_description = u'结余数量'

    def get_search_results(self, request, queryset, search_term):
        searchs = search_term.split('-')
        print("range:{}".format(range))
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
            queryset = self.model.objects.filter(balance_quantity__gte=number1, balance_quantity__lte=number2)
        return queryset, use_distinct

    def save_model(self, request, obj, form, change):
        put_num = obj.put_num
        push_num = obj.push_num
        unit_price = obj.unit_price
        obj.balance_quantity = put_num - push_num
        obj.total_price = put_num * unit_price
        super().save_formset(request, form, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
