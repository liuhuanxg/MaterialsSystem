# Generated by Django 3.2 on 2022-09-27 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('local_library', '0016_auto_20220904_1715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='localoutboundorder',
            options={'permissions': [('chaneg_is_ex', '是否可以地方库出库'), ('chaneg_is_check', '是否可以地方库核销')], 'verbose_name': '地方库出库单', 'verbose_name_plural': '地方库出库单'},
        ),
        migrations.AddField(
            model_name='localoutboundorder',
            name='applicant_phone',
            field=models.CharField(default='', max_length=100, verbose_name='领用人手机号'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='locallibrary',
            name='file',
            field=models.FileField(blank=True, upload_to='upload/local_library/2022/9/27', verbose_name='入库明细(excel)'),
        ),
        migrations.AlterField(
            model_name='localoutboundorder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='地方库供应商'),
        ),
        migrations.AlterField(
            model_name='localwarehousingfile',
            name='file',
            field=models.FileField(upload_to='upload/local_library/2022/9/27', verbose_name='(采购计划、政府采购批复、投标手续)'),
        ),
        migrations.AlterField(
            model_name='supplierfile',
            name='file',
            field=models.FileField(upload_to='upload/local_library/2022/9/27', verbose_name='(供应商附件)'),
        ),
    ]
