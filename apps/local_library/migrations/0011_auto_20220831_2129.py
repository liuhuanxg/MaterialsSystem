# Generated by Django 3.2 on 2022-08-31 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local_library', '0010_auto_20220830_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locallibrary',
            name='file',
            field=models.FileField(blank=True, upload_to='upload/local_library/2022/8/31', verbose_name='入库明细(excel)'),
        ),
        migrations.AlterField(
            model_name='localwarehousingfile',
            name='file',
            field=models.FileField(upload_to='upload/local_library/2022/8/31', verbose_name='(采购计划、政府采购批复、投标手续)'),
        ),
        migrations.AlterField(
            model_name='supplierfile',
            name='file',
            field=models.FileField(upload_to='upload/local_library/2022/8/31', verbose_name='(供应商附件)'),
        ),
    ]