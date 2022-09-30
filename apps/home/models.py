from django.contrib.auth.models import User, AbstractUser
from django.db import models

from utils.date_utils import get_date_str


class MaterialsType(models.Model):
    class Meta:
        verbose_name = "物料种类"
        verbose_name_plural = "物料种类"
        unique_together = ("materials_name", "specifications", "unit")
        ordering = ["-add_date"]

    materials_name = models.CharField("物料名称", max_length=100)
    specifications = models.CharField("规格", default="", max_length=512, blank=True)
    unit = models.CharField("单位", max_length=100, default="", blank=True)
    warning_quantity = models.FloatField("预警比例", default=10)
    des = models.TextField(verbose_name="描述", blank=True, default="")
    phone = models.CharField(verbose_name="供应商电话", max_length=20, blank=True, default="")
    add_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    add_date = models.DateField(verbose_name="创建日期", auto_now_add=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def __str__(self):
        return self.materials_name + "_" + self.specifications + "_" + self.unit


class CodeNumber(models.Model):
    class Meta:
        verbose_name = "单号自增表"
        verbose_name_plural = "单号自增表"

    db_name = models.CharField(verbose_name="数据表名称", max_length=100)
    date_str = models.CharField(verbose_name="日期", max_length=100)
    number = models.IntegerField(verbose_name="自增编号")

    @staticmethod
    def get_app_code(db_name):
        date_str = get_date_str()
        ware_app = CodeNumber.objects.filter(db_name=db_name, date_str=date_str).first()

        if ware_app:
            number = ware_app.number
            new_number = int(number) + 1
            if new_number < 10:
                code = "00{}".format(new_number)
            elif new_number < 100:
                code = "0{}".format(new_number)
            else:
                code = number
            ware_app.number = new_number
            ware_app.save()
        else:
            code = "001"
            number = 1
            CodeNumber.objects.create(date_str=date_str, db_name=db_name, number=number)
        app_code = date_str + str(code)
        return app_code
