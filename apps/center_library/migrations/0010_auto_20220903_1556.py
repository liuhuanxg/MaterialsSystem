# Generated by Django 3.2 on 2022-09-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center_library', '0009_auto_20220901_2046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='centeroutboundorder',
            options={'permissions': [('chaneg_is_ex', '是否可以出库'), ('chaneg_is_check', '是否可以核销')], 'verbose_name': '中央库出库单', 'verbose_name_plural': '中央库出库单'},
        ),
        migrations.AddField(
            model_name='centeroutboundorder',
            name='is_check',
            field=models.BooleanField(blank=True, default=False, verbose_name='是否核销'),
        ),
        migrations.AlterField(
            model_name='centerlibraryfile',
            name='file',
            field=models.FileField(upload_to='upload/center_library/2022/9/3', verbose_name='附件'),
        ),
        migrations.AlterField(
            model_name='centerwarehousingapplication',
            name='file',
            field=models.FileField(blank=True, upload_to='upload/center_library/2022/9/3', verbose_name='入库明细(excel)'),
        ),
        migrations.AlterField(
            model_name='centerwarehousingfile',
            name='file',
            field=models.FileField(upload_to='upload/center_library/2022/9/3', verbose_name='(采购计划、政府采购批复、投标手续)'),
        ),
    ]
