# Generated by Django 4.1 on 2022-08-27 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("local_library", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LocalLabraryMaterials",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("push_num", models.IntegerField(default=0, verbose_name="出库数量")),
                ("unit_price", models.FloatField(default=0, verbose_name="单价(元)")),
                (
                    "add_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                ("add_date", models.DateField(auto_now_add=True, verbose_name="创建日期")),
                (
                    "modify_time",
                    models.DateTimeField(auto_now=True, verbose_name="修改时间"),
                ),
            ],
            options={
                "verbose_name": "物料库存",
                "verbose_name_plural": "物料库存",
                "ordering": ["-add_time"],
            },
        ),
        migrations.CreateModel(
            name="LocalLibrary",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "app_code",
                    models.CharField(max_length=100, unique=True, verbose_name="入库单号"),
                ),
                (
                    "entry_name",
                    models.CharField(max_length=100, unique=True, verbose_name="项目名称"),
                ),
                ("budget", models.FloatField(default=0, verbose_name="预算(万)")),
                ("less_budget", models.FloatField(default=0, verbose_name="剩余预算(万)")),
                (
                    "des",
                    models.CharField(blank=True, max_length=100, verbose_name="描述"),
                ),
                (
                    "add_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="创建时间"
                    ),
                ),
                (
                    "add_date",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="创建日期"
                    ),
                ),
                (
                    "modify_time",
                    models.DateTimeField(auto_now=True, verbose_name="修改时间"),
                ),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        upload_to="upload/local_library/2022/8/27",
                        verbose_name="物资附件",
                    ),
                ),
                ("is_approve", models.BooleanField(default=0, verbose_name="是否审核")),
            ],
            options={
                "verbose_name": "入库单",
                "verbose_name_plural": "入库单",
                "permissions": [("can_approve", "是否可以审核入库单")],
            },
        ),
        migrations.CreateModel(
            name="LocalOutboundOrder",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(default="", max_length=100, verbose_name="申请主题"),
                ),
                (
                    "applicant",
                    models.CharField(default="", max_length=100, verbose_name="申请单位"),
                ),
                (
                    "applicant_user",
                    models.CharField(
                        default="", max_length=100, unique=True, verbose_name="领用人"
                    ),
                ),
                (
                    "des",
                    models.CharField(
                        blank=True, default="", max_length=100, verbose_name="申请说明"
                    ),
                ),
                (
                    "total_price",
                    models.FloatField(blank=True, default=0, verbose_name="总金额"),
                ),
                (
                    "is_ex",
                    models.BooleanField(blank=True, default=False, verbose_name="是否出库"),
                ),
                (
                    "add_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="申请时间"
                    ),
                ),
                ("add_date", models.DateField(auto_now_add=True, verbose_name="申请日期")),
            ],
            options={"verbose_name": "地方库库出库单", "verbose_name_plural": "中央库出库单",},
        ),
        migrations.CreateModel(
            name="LocalOutboundOrderDetail",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "library_name",
                    models.CharField(max_length=1000, verbose_name="物资类型"),
                ),
                ("number", models.IntegerField(default=0, verbose_name="领用数量")),
            ],
            options={"verbose_name": "地方库库出库单详情", "verbose_name_plural": "地方库库出库单详情",},
        ),
        migrations.CreateModel(
            name="SupplierMessage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "company_name",
                    models.CharField(default="", max_length=100, verbose_name="公司名称"),
                ),
                (
                    "supplier_des",
                    models.CharField(
                        blank=True, default="", max_length=100, verbose_name="供应商描述"
                    ),
                ),
                (
                    "add_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "modify_time",
                    models.DateTimeField(auto_now=True, verbose_name="修改时间"),
                ),
                ("add_date", models.DateField(auto_now_add=True, verbose_name="创建日期")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
            ],
            options={"verbose_name": "地方库", "verbose_name_plural": "地方库",},
        ),
        migrations.CreateModel(
            name="SupplierFile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="upload/local_library/2022/8/27",
                        verbose_name="(供应商附件)",
                    ),
                ),
                (
                    "add_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "library_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="local_library.suppliermessage",
                        verbose_name="申请单编号",
                    ),
                ),
            ],
            options={"verbose_name": "(供应商附件)", "verbose_name_plural": "(供应商附件)",},
        ),
        migrations.CreateModel(
            name="LocalWarehousingFile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="upload/local_library/2022/8/27",
                        verbose_name="(采购计划、政府采购批复、投标手续)",
                    ),
                ),
                (
                    "add_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "library_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="local_library.locallibrary",
                        verbose_name="申请单编号",
                    ),
                ),
            ],
            options={
                "verbose_name": "(采购计划、政府采购批复、投标手续)",
                "verbose_name_plural": "(采购计划、政府采购批复、投标手续)",
            },
        ),
        migrations.CreateModel(
            name="LocalOutboundOrderHistory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "application_user",
                    models.CharField(blank=True, max_length=20, verbose_name="操作人"),
                ),
                (
                    "action",
                    models.CharField(default="通过", max_length=20, verbose_name="审批动作"),
                ),
                (
                    "add_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="审批时间"
                    ),
                ),
                (
                    "application",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="local_library.localoutboundorder",
                        verbose_name="申请单",
                    ),
                ),
            ],
            options={"verbose_name": "审批记录", "verbose_name_plural": "审批记录",},
        ),
    ]
