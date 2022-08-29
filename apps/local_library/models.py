from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from utils.date_utils import upload_path_handler


# 地方库信息
class LocalLibrary(models.Model):
    class Meta:
        verbose_name = "入库单"
        verbose_name_plural = "入库单"
        permissions = [("can_approve", "是否可以审核入库单")]

    app_code = models.CharField("入库单号", unique=True, max_length=100)
    entry_name = models.CharField("项目名称", unique=True, max_length=100)
    budget = models.FloatField("预算(万元)", default=0)
    less_budget = models.FloatField("剩余预算(万元)", default=0)
    supplier_name = models.ForeignKey("SupplierMessage", verbose_name="供应商", on_delete=models.DO_NOTHING)
    des = models.CharField(verbose_name="入库描述", blank=True, max_length=100)
    add_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)
    add_date = models.DateField(verbose_name="创建日期", default=timezone.now)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    create_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="创建人", blank=True,
                                    related_name="create_user")
    file = models.FileField(verbose_name="入库明细(excel)", upload_to=upload_path_handler("local_library"), blank=True)
    is_approve = models.BooleanField(verbose_name="审核通过", default=0)

    def __str__(self):
        return self.entry_name


class SupplierMessage(models.Model):
    class Meta:
        verbose_name = "地方库"
        verbose_name_plural = "地方库"

    company_name = models.CharField(verbose_name="公司名称", max_length=100, default="")
    user = models.OneToOneField(User, verbose_name="用户", on_delete=models.DO_NOTHING)
    supplier_des = models.CharField(verbose_name="供应商描述", max_length=100, blank=True, default="")
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    add_date = models.DateField(verbose_name="创建日期", auto_now_add=True)

    def __str__(self):
        return self.company_name


class SupplierFile(models.Model):
    class Meta:
        verbose_name = "(供应商附件)"
        verbose_name_plural = "(供应商附件)"

    file = models.FileField(verbose_name="(供应商附件)", upload_to=upload_path_handler("local_library"))
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    library_name = models.ForeignKey("SupplierMessage", on_delete=models.DO_NOTHING, verbose_name="供应商")


class LocalLabraryMaterials(models.Model):
    class Meta:
        verbose_name = "物料库存"
        verbose_name_plural = "物料库存"
        unique_together = ("library_name", "type_name")
        ordering = ["-add_time"]

    library_name = models.ForeignKey("LocalLibrary", on_delete=models.DO_NOTHING, verbose_name="项目名称")
    type_name = models.ForeignKey("home.MaterialsType", on_delete=models.DO_NOTHING, verbose_name="物资类型")
    push_num = models.IntegerField("出库数量", default=0)
    unit_price = models.FloatField("单价(元)", default=0)
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    add_date = models.DateField(verbose_name="创建日期", auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def __str__(self):
        return (self.library_name.entry_name + "_" + self.type_name.materials_name
                + "_" + self.type_name.specifications + "_" + self.type_name.unit + "(单价(元):"
                + str(self.unit_price) + ")" + "剩余预算(万元):" + str(self.library_name.less_budget)
                )


class LocalWarehousingFile(models.Model):
    class Meta:
        verbose_name = "(采购计划、政府采购批复、投标手续)"
        verbose_name_plural = "(采购计划、政府采购批复、投标手续)"

    file = models.FileField(verbose_name="(采购计划、政府采购批复、投标手续)", upload_to=upload_path_handler("local_library"))
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    library_name = models.ForeignKey("LocalLibrary", on_delete=models.DO_NOTHING, verbose_name="入库单编号")

    def __str__(self):
        return str(self.id)


class LocalOutboundOrder(models.Model):
    class Meta:
        verbose_name = "地方库库出库单"
        verbose_name_plural = "地方库库出库单"
        unique_together = ["app_code", "user"]

    app_code = models.OneToOneField("material_application.ExWarehousingApplication", on_delete=models.DO_NOTHING,
                                    verbose_name="出库单")
    user = models.ForeignKey(User, verbose_name="供应商", on_delete=models.DO_NOTHING)
    title = models.CharField("申请主题", max_length=100, default="")
    applicant = models.CharField("申请单位", max_length=100, default="")
    applicant_user = models.CharField("领用人", unique=True, max_length=100, default="")
    des = models.CharField("申请说明", blank=True, max_length=100, default="")
    total_price = models.FloatField("总金额(元)", blank=True, default=0)
    is_ex = models.BooleanField(verbose_name="是否出库", default=False, blank=True)
    add_time = models.DateTimeField(verbose_name="申请时间", default=timezone.now)
    add_date = models.DateField(verbose_name="申请日期", auto_now_add=True)

    def __str__(self):
        return str(self.app_code.app_code)

class LocalOutboundOrderDetail(models.Model):
    class Meta:
        verbose_name = "地方库库出库单详情"
        verbose_name_plural = "地方库库出库单详情"
        unique_together = ["app_code", "assessment_detail"]

    app_code = models.ForeignKey("LocalOutboundOrder", on_delete=models.DO_NOTHING, verbose_name="出库单")
    assessment_detail = models.OneToOneField("material_application.LocalAssessmentDetail", on_delete=models.DO_NOTHING,
                                             verbose_name="物资详情")
    number = models.IntegerField(default=0, verbose_name="数量")
    total_price = models.FloatField(default=0, verbose_name="金额(元)")
    def __str__(self):
        return str(self.app_code.app_code)


class LocalOutboundOrderHistory(models.Model):
    class Meta:
        verbose_name = "审批记录"
        verbose_name_plural = "审批记录"
        unique_together = ["application", "history_detail"]

    application = models.ForeignKey("LocalOutboundOrder", on_delete=models.DO_NOTHING, verbose_name="申请单")
    history_detail = models.OneToOneField("material_application.ApplicationHistory", on_delete=models.DO_NOTHING,
                                          verbose_name="申请单")
    application_user = models.CharField(max_length=20, blank=True, verbose_name="操作人")
    action = models.CharField(max_length=20, default="通过", verbose_name="审批意见")
    add_time = models.DateField(verbose_name="审批时间", default=timezone.now)

    def __str__(self):
        return str(self.id)
