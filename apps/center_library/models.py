from django.contrib.auth.models import User
from django.db import models

from utils.date_utils import upload_path_handler

# 中央库基本信息
class CenterLibrary(models.Model):
    class Meta:
        verbose_name = "中央库基本信息"
        verbose_name_plural = "中央库基本信息"

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


# 入库单信息
class CenterWarehousingApplication(models.Model):
    class Meta:
        verbose_name = "入库单"
        verbose_name_plural = "入库单"

    app_code = models.CharField("入库单号", unique=True, max_length=15)
    # app_code = models.CharField("项目名称", unique=True, max_length=15)
    total_price = models.FloatField(verbose_name="入库总金额(万元)", default=0)
    des = models.CharField(verbose_name="描述", blank=True, max_length=100)
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    add_date = models.DateField(verbose_name="创建日期", auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    create_u = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="创建人", blank=True,
                                 related_name="create_u")

    def __str__(self):
        return self.app_code


class CenterLabraryMaterials(models.Model):
    class Meta:
        verbose_name = "入库明细"
        verbose_name_plural = "入库明细"
        unique_together = ("ware_app", "type_name")

    type_name = models.ForeignKey("home.MaterialsType", on_delete=models.DO_NOTHING, verbose_name="类型名称")
    ware_app = models.ForeignKey(CenterWarehousingApplication, on_delete=models.DO_NOTHING, verbose_name="入库单")
    put_num = models.IntegerField("入库数量", default=0)
    unit_price = models.FloatField("单价(元)", default=0)
    total_price = models.FloatField("总金额(元)", default=0, blank=True)
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    add_date = models.DateField(verbose_name="创建日期", auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def __str__(self):
        return str(self.id)

    def clean(self):
        super(CenterLabraryMaterials, self).clean()
        self.total_price = self.unit_price * self.put_num


class CenterLabraryQuantity(models.Model):
    class Meta:
        verbose_name = "物料库存"
        verbose_name_plural = "物料库存"

    type_name = models.OneToOneField("home.MaterialsType", on_delete=models.DO_NOTHING, verbose_name="类型名称")
    put_num = models.IntegerField("入库数量", default=0)
    push_num = models.IntegerField("出库数量", default=0)
    balance_num = models.IntegerField("结余数量", default=0)
    total_price = models.FloatField("该物资入库总金额(元)", default=0, blank=True)
    out_price = models.FloatField("该物资出库总金额(元)", default=0, blank=True)

    def __str__(self):
        return str(self.id)


class CenterWarehousingFile(models.Model):
    class Meta:
        verbose_name = "(采购计划、政府采购批复、投标手续)等附件"
        verbose_name_plural = "(采购计划、政府采购批复、投标手续)等附件"

    file = models.FileField(verbose_name="(采购计划、政府采购批复、投标手续)", upload_to=upload_path_handler("center_library"))
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    library_name = models.ForeignKey("CenterWarehousingApplication", on_delete=models.DO_NOTHING, verbose_name="申请单编号")
