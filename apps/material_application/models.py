from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from MaterialsSystem.settings import status_choices
from utils.date_utils import upload_path_handler


class ExWarehousingApplication(models.Model):
    class Meta:
        verbose_name = "出库申请单"
        verbose_name_plural = "出库申请单"

    title = models.CharField("申请标题", unique=True, max_length=100)
    applicant = models.CharField("申请单位", max_length=100)
    applicant_user = models.CharField("领用人", unique=True, max_length=100)
    des = models.CharField("申请说明", blank=True, max_length=100)
    add_time = models.DateTimeField(verbose_name="申请时间", auto_now_add=True)
    add_date = models.DateField(verbose_name="申请日期", auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    create_user = models.ForeignKey(User, verbose_name="创建人", on_delete=models.DO_NOTHING, blank=True)
    status = models.CharField(verbose_name="状态", blank=True, choices=status_choices, max_length=5, default="1")
    next_node = models.CharField(verbose_name="下一个审批人", max_length=100, default="")

    def __str__(self):
        return self.title


class ExApplicationFile(models.Model):
    class Meta:
        verbose_name = "附件"
        verbose_name_plural = "附件"

    file = models.FileField(verbose_name="附件", upload_to=upload_path_handler("center_library"))
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    library_name = models.ForeignKey("ExWarehousingApplication", on_delete=models.DO_NOTHING, verbose_name="申请单编号")


class ApplicationDetail(models.Model):
    class Meta:
        verbose_name = "领用详情"
        verbose_name_plural = "领用详情"

    type_name = models.ForeignKey("home.MaterialsType", on_delete=models.DO_NOTHING, verbose_name="物资类型")
    application = models.ForeignKey("ExWarehousingApplication", on_delete=models.DO_NOTHING, verbose_name="申请单",
                                    default="")
    number = models.IntegerField(verbose_name="领用数量", default=0)
    assessments = models.ForeignKey("Assessments", on_delete=models.DO_NOTHING, verbose_name="研判记录", )

    def clean(self):
        if self.number <= 0:
            raise ValidationError("领用数量不能小于1")

    def __str__(self):
        return self.type_name.materials_name + "_" + str(self.number)


class ApplicationHistory(models.Model):
    class Meta:
        verbose_name = "审批记录"
        verbose_name_plural = "审批记录"

    application = models.ForeignKey("ExWarehousingApplication", on_delete=models.DO_NOTHING, verbose_name="申请单")
    add_time = models.DateTimeField(verbose_name="审批时间", auto_now_add=True)


class Assessments(models.Model):
    class Meta:
        verbose_name = "主管科室研判"
        verbose_name_plural = "主管科室研判"

    application = models.ForeignKey("ExWarehousingApplication", on_delete=models.DO_NOTHING, verbose_name="申请单")
    title = models.CharField("申请标题", unique=True, max_length=100)
    applicant = models.CharField("申请单位", max_length=100)
    applicant_user = models.CharField("领用人", unique=True, max_length=100)
    des = models.TextField("申请说明", blank=True)
    add_time = models.DateTimeField(verbose_name="申请时间", auto_now_add=True)
    add_date = models.DateField(verbose_name="申请日期", auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    create_user = models.ForeignKey(User, verbose_name="创建人", on_delete=models.DO_NOTHING, blank=True)
    number = models.IntegerField(verbose_name="领用数量", default=0)


class AssessmentDetail(models.Model):
    class Meta:
        verbose_name = "主管科室研判详情"
        verbose_name_plural = "主管科室研判详情"

    type_name = models.ForeignKey("home.MaterialsType", on_delete=models.DO_NOTHING, verbose_name="物资类型")
    application = models.ForeignKey("Assessments", on_delete=models.DO_NOTHING, verbose_name="申请单")
    number = models.IntegerField(verbose_name="领用数量", default=0)
