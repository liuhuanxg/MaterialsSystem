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
    des = models.CharField("原因描述", blank=True, max_length=100)
    add_time = models.DateTimeField(verbose_name="申请时间", default=timezone.now)
    add_date = models.DateField(verbose_name="申请日期", auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    create_user = models.ForeignKey(User, verbose_name="创建人", on_delete=models.DO_NOTHING, blank=True)
    status = models.CharField(verbose_name="状态", blank=True, choices=status_choices, max_length=5, default="1")
    next_node = models.CharField(verbose_name="下一个审批人", max_length=100, default="")

    def __str__(self):
        return self.app_code + "——" + str(self.title)

    # def clean(self):
    #     center_assessment_details = CenterAssessmentDetail.objects.filter(application_id=self.id)
    #     local_assessment_details = LocalAssessmentDetail.objects.filter(application_id=self.id)
    #     all_assessment_details = {}
    #     for center_assessment_detail in center_assessment_details:
    #         type_name_id = center_assessment_detail.library_name.type_name.id
    #         all_assessment_details[type_name_id] = all_assessment_details.get(type_name_id,
    #                                                                           0) + center_assessment_detail.number
    #     for local_assessment_detail in local_assessment_details:
    #         type_name_id = local_assessment_detail.library_name.type_name_id
    #
    #         all_assessment_details[type_name_id] = all_assessment_details.get(type_name_id,
    #                                                                           0) + local_assessment_detail.number
    #     print("self_id:{},all_assessment_details:{}".format(self.id, all_assessment_details))
    #     if all_applications_details != all_assessment_details:
    #         raise ValidationError("研判数量和申请数量不符。")


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
    application = models.ForeignKey("ExWarehousingApplication", on_delete=models.DO_NOTHING, verbose_name="申请单")
    number = models.IntegerField(verbose_name="领用数量", default=0)

    def clean(self):
        app = ApplicationDetail.objects.filter(id=self.id).first()
        if app:
            print("clean ApplicationDetail obj_id:{}, obj_status:{}, new_status:{}, obj_number:{}, new_number:{}".format(
                self.id, app.application.status, self.application.status, app.number, self.number,
            ))
        # TODO(发起人也不能修改数量，有bug)
        if app and int(self.application.status) != 1 and self.number > app.number:
            raise ValidationError("领用数量不能增大")
        if self.number <= 0:
            raise ValidationError("领用数量不能小于1")

    def __str__(self):
        return self.type_name.materials_name + "_" + str(self.number)


class ApplicationHistory(models.Model):
    class Meta:
        verbose_name = "审批记录"
        verbose_name_plural = "审批记录"
        ordering = ["-add_time"]

    application = models.ForeignKey("ExWarehousingApplication", on_delete=models.DO_NOTHING, verbose_name="申请单")
    application_user = models.CharField(max_length=20, blank=True, verbose_name="审批人")
    action = models.CharField(max_length=20, default="通过", verbose_name="审批动作")
    add_time = models.DateField(verbose_name="操作日期", default=timezone.now)

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
    total_price = models.FloatField(verbose_name="领用金额(元)", default=0)
    is_ex = models.BooleanField(verbose_name="是否出库", default=0)
    add_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)

    def __str__(self):
        return (self.library_name.library_name.entry_name + "_" + self.library_name.type_name.materials_name
                + "_" + self.library_name.type_name.specifications + "_" + self.library_name.type_name.unit
                )

    def clean(self):
        if self.number <= 0:
            raise ValidationError("领用数量不能小于1")


class CenterAssessmentDetail(models.Model):
    class Meta:
        verbose_name = "中央库研判"
        verbose_name_plural = "中央库研判"

    library_name = models.ForeignKey("center_library.CenterLabraryQuantity", on_delete=models.DO_NOTHING,
                                     verbose_name="物资类型")
    application = models.ForeignKey("ExWarehousingApplication", on_delete=models.DO_NOTHING, verbose_name="申请单")
    number = models.IntegerField(verbose_name="领用数量", default=0)
    is_ex = models.BooleanField(verbose_name="是否出库", default=0)
    add_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)

    def __str__(self):
        return str(self.id)

    def clean(self):
        if self.number <= 0:
            raise ValidationError("领用数量不能小于1")


class Accounts(models.Model):
    class Meta:
        verbose_name = "台账"
        verbose_name_plural = "台账"
        unique_together = ("app_code", "entry_name", "type_name", "specifications", "unit", "db_type")

    type_choice = (
        ("1", "地方库"),
        ("2", "中央库")
    )
    action_choice = (
        ("1", "入库"),
        ("2", "出库")
    )
    app_code = models.CharField(verbose_name="单号", max_length=100)
    db_type = models.CharField(verbose_name="库类型", choices=type_choice, max_length=10)
    entry_name = models.CharField(verbose_name="项目名称", max_length=100)
    type_name = models.CharField(verbose_name="类型名称", max_length=100)
    specifications = models.CharField(verbose_name="规格", max_length=100, default="")
    unit = models.CharField(verbose_name="单位", max_length=100, default="")
    action = models.CharField(verbose_name="操作名称", choices=action_choice, max_length=10)
    number = models.IntegerField(verbose_name="数量", default=0)
    price = models.FloatField(verbose_name="金额(元)", default=0)
    unit_price = models.FloatField(verbose_name="单价(元)", default=None)
    add_time = models.DateTimeField(verbose_name="时间", default=timezone.now)
    add_date = models.DateField(verbose_name="日期", default=timezone.now)

    @staticmethod
    def save_one(app_code, entry_name, type_name, specifications, unit, action, unit_price, number=0, price=0,
                 db_type="1"):
        """
        :param app_code: 单号
        :param db_name: 项目名称
        :param type_name: 种类名称
        :param action: 动作
        :param number: 数量
        :param price: 加个
        :param db_type: 数据库类型
        :return:
        """
        accounts = Accounts.objects.filter(
            app_code=app_code,
            entry_name=entry_name,
            type_name=type_name,
            specifications=specifications,
            unit=unit,
            db_type=db_type,
        )
        if accounts.exists():
            accounts.update(number=number, price=price, unit_price=unit_price)
        else:
            a = Accounts()
            a.app_code = app_code
            a.entry_name = entry_name
            a.type_name = type_name
            a.specifications = specifications
            a.unit = unit
            a.action = action
            a.number = number
            a.price = price
            a.db_type = db_type
            a.unit_price = unit_price
            a.save()