from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from MaterialsSystem.settings import status_choices
from utils.date_utils import upload_path_handler


class ExWarehousingApplication(models.Model):
    class Meta:
        verbose_name = "出库申请"
        verbose_name_plural = "出库申请"

    app_code = models.CharField("申请单号", unique=True, max_length=100)
    title = models.CharField("申请主题", unique=True, max_length=100)
    applicant = models.CharField("申请单位", max_length=100)
    applicant_user = models.CharField("领用人", unique=True, max_length=100)
    des = models.CharField("申请说明", blank=True, max_length=100)
    add_time = models.DateTimeField(verbose_name="申请时间", default=timezone.now)
    add_date = models.DateField(verbose_name="申请日期", auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    create_user = models.ForeignKey(User, verbose_name="创建人", on_delete=models.DO_NOTHING, blank=True)
    status = models.CharField(verbose_name="状态", blank=True, choices=status_choices, max_length=5, default="1")
    next_node = models.CharField(verbose_name="下一个审批人", max_length=100, default="")

    def __str__(self):
        return self.title


class ExApplicationFile(models.Model):
    class Meta:
        verbose_name = "申请资料"
        verbose_name_plural = "申请资料"

    file = models.FileField(verbose_name="申请资料", upload_to=upload_path_handler("center_library"))
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    library_name = models.ForeignKey("ExWarehousingApplication", on_delete=models.DO_NOTHING, verbose_name="申请单编号")


class ApplicationDetail(models.Model):
    class Meta:
        verbose_name = "领用详情"
        verbose_name_plural = "领用详情"

    type_name = models.ForeignKey("home.MaterialsType", on_delete=models.DO_NOTHING, verbose_name="物资类型")
    application = models.ForeignKey("ExWarehousingApplication", on_delete=models.CASCADE, verbose_name="申请单")
    number = models.IntegerField(verbose_name="领用数量", default=0)

    def clean(self):
        app = ApplicationDetail.objects.filter(id=self.id).first()
        if app and self.number > app.number:
            raise ValidationError("领用数量不能增大")
        if self.number <= 0:
            raise ValidationError("领用数量不能小于1")

    def __str__(self):
        return self.type_name.materials_name + "_" + str(self.number)


class ApplicationHistory(models.Model):
    class Meta:
        verbose_name = "审批记录"
        verbose_name_plural = "审批记录"

    application = models.ForeignKey("ExWarehousingApplication", on_delete=models.DO_NOTHING, verbose_name="申请单")
    application_user = models.CharField(max_length=20, blank=True, verbose_name="审批人")
    action = models.CharField(max_length=20, default="通过", verbose_name="审批动作")
    add_time = models.DateTimeField(verbose_name="审批时间", default=timezone.now)

    def __str__(self):
        return str(self.id)


class LocalAssessmentDetail(models.Model):
    class Meta:
        verbose_name = "地方库研判"
        verbose_name_plural = "地方库研判"

    library_name = models.ForeignKey("local_library.LocalLabraryMaterials", on_delete=models.DO_NOTHING,
                                     verbose_name="物资类型")
    application = models.ForeignKey("ExWarehousingApplication", on_delete=models.DO_NOTHING, verbose_name="申请单")
    number = models.IntegerField(verbose_name="领用数量", default=0)
    def __str__(self):
        return str(self.id)

class CenterAssessmentDetail(models.Model):
    class Meta:
        verbose_name = "中央库研判"
        verbose_name_plural = "中央库研判"

    library_name = models.ForeignKey("center_library.CenterLabraryQuantity", on_delete=models.DO_NOTHING,
                                     verbose_name="物资类型")
    application = models.ForeignKey("ExWarehousingApplication", on_delete=models.DO_NOTHING, verbose_name="申请单")
    number = models.IntegerField(verbose_name="领用数量", default=0)

    def __str__(self):
        return str(self.id)