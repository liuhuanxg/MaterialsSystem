from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from utils.date_utils import upload_path_handler


# 地方库信息
class LocalLibrary(models.Model):
    class Meta:
        verbose_name = "地方库"
        verbose_name_plural = "地方库"
        permissions = [("can_approve", "是否可以审核入库单")]

    app_code = models.CharField("入库单号", unique=True, max_length=100)
    entry_name = models.CharField("项目名称", unique=True, max_length=100)
    supplier_name = models.ForeignKey("SupplierMessage", verbose_name="供应商", on_delete=models.DO_NOTHING)
    des = models.CharField(verbose_name="描述", blank=True, max_length=100)
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, default=timezone.now)
    add_date = models.DateField(verbose_name="创建日期", default=timezone.now)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    create_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="创建人", blank=True,
                                    related_name="create_user")
    is_approve = models.BooleanField(verbose_name="是否审核", default=0)

    def __str__(self):
        return self.app_code


class SupplierMessage(models.Model):
    class Meta:
        verbose_name = "供应商信息"
        verbose_name_plural = "供应商信息"

    company_name = models.CharField(verbose_name="公司名称", max_length=100, unique=True)
    user = models.OneToOneField(User, verbose_name="用户", on_delete=models.DO_NOTHING)
    supplier_des = models.CharField(verbose_name="供应商描述", max_length=100, blank=True)
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    add_date = models.DateField(verbose_name="创建日期", auto_now_add=True)

    def __str__(self):
        return self.company_name

class SupplierFile(models.Model):
    class Meta:
        verbose_name = "(供应商附件)"
        verbose_name_plural = "(供应商附件)"

    file = models.FileField(verbose_name="(供应商附件)", upload_to=upload_path_handler("center_library"))
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    library_name = models.ForeignKey("SupplierMessage", on_delete=models.DO_NOTHING, verbose_name="申请单编号")


class LocalLabraryMaterials(models.Model):
    class Meta:
        verbose_name = "物料库存"
        verbose_name_plural = "物料库存"
        unique_together = ("ware_app", "type_name")
        ordering = ["-add_time"]

    library_name = models.ForeignKey("LocalLibrary", on_delete=models.DO_NOTHING, verbose_name="库名")
    type_name = models.ForeignKey("home.MaterialsType", on_delete=models.DO_NOTHING, verbose_name="物资类型")
    push_num = models.IntegerField("出库数量", default=0)
    unit_price = models.FloatField("单价(元)", default=0)
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    add_date = models.DateField(verbose_name="创建日期", auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def __str__(self):
        return str(self.id)


class LocalWarehousingFile(models.Model):
    class Meta:
        verbose_name = "(采购计划、政府采购批复、投标手续)"
        verbose_name_plural = "(采购计划、政府采购批复、投标手续)"

    file = models.FileField(verbose_name="(采购计划、政府采购批复、投标手续)", upload_to=upload_path_handler("center_library"))
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    library_name = models.ForeignKey("LocalLibrary", on_delete=models.DO_NOTHING, verbose_name="申请单编号")
