# Generated by Django 3.2 on 2022-08-30 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center_library', '0006_auto_20220829_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centerlibraryfile',
            name='file',
            field=models.FileField(upload_to='upload/center_library/2022/8/30', verbose_name='附件'),
        ),
        migrations.AlterField(
            model_name='centerwarehousingapplication',
            name='file',
            field=models.FileField(blank=True, upload_to='upload/center_library/2022/8/30', verbose_name='入库明细(excel)'),
        ),
        migrations.AlterField(
            model_name='centerwarehousingfile',
            name='file',
            field=models.FileField(upload_to='upload/center_library/2022/8/30', verbose_name='(采购计划、政府采购批复、投标手续)'),
        ),
    ]
