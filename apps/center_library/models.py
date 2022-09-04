from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from utils.date_utils import upload_path_handler


# 中央库基本信息
class CenterLibrary(models.Model):
    class Meta:
        verbose_name = "中央库基本信息"
        verbose_name_plural = "中央库基本信息"
        ordering = ["-add_date"]

    library_name = models.CharField("中央库名称", unique=True, max_length=100)
    total_budget = models.FloatField(verbose_name="总预算(万元)", default=0)
    des = models.CharField(verbose_name="中央库描述信息", blank=True, max_length=100)
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    add_date = models.DateField(verbose_name="创建日期", auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    create_user = models.ForeignKey(User, verbose_name="创建人", on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return self.library_name


class CenterLibraryFile(models.Model):
    class Meta:
        verbose_name = "中央库附件"
        verbose_name_plural = "中央库附件"

    file = models.FileField(verbose_name="附件", upload_to=upload_path_handler("center_library"))
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    library_name = models.ForeignKey("CenterLibrary", on_delete=models.DO_NOTHING, verbose_name="库名")

    def __str__(self):
        return ""

# 入库单信息
class CenterWarehousingApplication(models.Model):
    class Meta:
        verbose_name = "中央库入库单"
        verbose_name_plural = "中央库入库单"
        ordering = ["-add_date"]

    app_code = models.CharField("入库单号", unique=True, max_length=15)
    total_price = models.FloatField(verbose_name="入库总金额(万元)", default=0)
    des = models.CharField(verbose_name="描述", blank=True, max_length=100)
    add_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)
    add_date = models.DateField(verbose_name="创建日期", auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    create_u = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="创建人", blank=True,
                                 related_name="create_u")
    file = models.FileField(verbose_name="入库明细(excel)", upload_to=upload_path_handler("center_library"), blank=True)

    def __str__(self):
        return self.app_code


class CenterLabraryMaterials(models.Model):
    class Meta:
        verbose_name = "入库明细"
        verbose_name_plural = "入库明细"
        unique_together = ("ware_app", "type_name")
        ordering = ["-add_time"]

    type_name = models.ForeignKey("home.MaterialsType", on_delete=models.DO_NOTHING, verbose_name="类型名称")
    ware_app = models.ForeignKey(CenterWarehousingApplication, on_delete=models.DO_NOTHING, verbose_name="入库单")
    put_num = models.IntegerField("入库数量", default=0)
    unit_price = models.FloatField("单价(元)", default=0)
    total_price = models.FloatField("总金额(元)", default=0, blank=True)
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    add_date = models.DateField(verbose_name="创建日期", auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def __str__(self):
        return ""

    def clean(self):
        super(CenterLabraryMaterials, self).clean()
        self.total_price = self.unit_price * self.put_num


class CenterLabraryQuantity(models.Model):
    class Meta:
        verbose_name = "中央库物料库存"
        verbose_name_plural = "中央库物料库存"

    type_name = models.OneToOneField("home.MaterialsType", on_delete=models.DO_NOTHING, verbose_name="类型名称")
    put_num = models.IntegerField("入库数量", default=0)
    push_num = models.IntegerField("出库数量", default=0)
    balance_num = models.IntegerField("结余数量", default=0)
    total_price = models.FloatField("该物资入库总金额(元)", default=0, blank=True)
    out_price = models.FloatField("该物资出库总金额(元)", default=0, blank=True)
    unit_price = models.FloatField(verbose_name="单价(元)", default=0, blank=True)

    def __str__(self):
        return (self.type_name.materials_name + "_" +
                self.type_name.specifications + "_" +
                self.type_name.unit + "剩余：" + str(self.balance_num)+
                "单价(元):"+str(self.unit_price)
                )


class CenterWarehousingFile(models.Model):
    class Meta:
        verbose_name = "(采购计划、政府采购批复、投标手续)等附件"
        verbose_name_plural = "(采购计划、政府采购批复、投标手续)等附件"

    file = models.FileField(verbose_name="(采购计划、政府采购批复、投标手续)", upload_to=upload_path_handler("center_library"))
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    library_name = models.ForeignKey("CenterWarehousingApplication", on_delete=models.DO_NOTHING, verbose_name="申请单编号")


class CenterOutboundOrder(models.Model):
    class Meta:
        verbose_name = "中央库出库单"
        verbose_name_plural = "中央库出库单"
        permissions = [
            ("chaneg_is_ex", "是否可以中央库出库"),
            ("chaneg_is_check", "是否可以中央库核销"),
        ]

    app_code = models.OneToOneField("material_application.ExWarehousingApplication", on_delete=models.DO_NOTHING,
                                    verbose_name="出库单")
    title = models.CharField("申请主题", max_length=100, default="")
    total_price = models.FloatField("出库金额", default=0)
    applicant = models.CharField("申请单位", max_length=100, default="")
    applicant_user = models.CharField("领用人", max_length=100, default="")
    des = models.CharField("申请说明", blank=True, max_length=100, default="")
    is_ex = models.BooleanField(verbose_name="是否出库", default=False, blank=True)
    is_check = models.BooleanField(verbose_name="是否核销", default=False, blank=True)
    add_time = models.DateTimeField(verbose_name="申请时间", default=timezone.now)
    add_date = models.DateField(verbose_name="申请日期", auto_now_add=True)


class CenterOutboundOrderDetail(models.Model):
    class Meta:
        verbose_name = "中央库出库单详情"
        verbose_name_plural = "中央库出库单详情"
        unique_together = ["app_code", "assessment_detail"]

    app_code = models.ForeignKey("CenterOutboundOrder", on_delete=models.DO_NOTHING, verbose_name="出库单")
    assessment_detail = models.OneToOneField("material_application.CenterAssessmentDetail", on_delete=models.DO_NOTHING,
                                             verbose_name="研判详情")
    number = models.IntegerField(verbose_name="领用数量", default=0)
    total_price = models.FloatField(verbose_name="金额", default=0)

    def __str__(self):
        return ""


class CenterOutboundOrderHistory(models.Model):
    class Meta:
        verbose_name = "审批记录"
        verbose_name_plural = "审批记录"
        unique_together = ["application", "history_detail"]

    application = models.ForeignKey("CenterOutboundOrder", on_delete=models.DO_NOTHING, verbose_name="申请单")
    history_detail = models.OneToOneField("material_application.ApplicationHistory", on_delete=models.DO_NOTHING,
                                          verbose_name="申请单")
    application_user = models.CharField(max_length=20, blank=True, verbose_name="操作人")
    action = models.CharField(max_length=20, default="通过", verbose_name="审批动作")
    add_time = models.DateTimeField(verbose_name="审批时间", default=timezone.now)

    def __str__(self):
        return ""
