# Generated by Django 3.2 on 2022-09-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center_library', '0013_alter_centeroutboundorder_applicant_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='centeroutboundorder',
            options={'permissions': [('chaneg_is_ex', '是否可以中央库出库'), ('chaneg_is_check', '是否可以中央库核销')], 'verbose_name': '中央库出库单', 'verbose_name_plural': '中央库出库单'},
        ),
        migrations.AddField(
            model_name='centeroutboundorder',
            name='applicant_phone',
            field=models.CharField(default='', max_length=100, verbose_name='领用人手机号'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='centerlibraryfile',
            name='file',
            field=models.FileField(upload_to='upload/center_library/2022/9/27', verbose_name='附件'),
        ),
        migrations.AlterField(
            model_name='centerwarehousingapplication',
            name='file',
            field=models.FileField(blank=True, upload_to='upload/center_library/2022/9/27', verbose_name='入库明细(excel)'),
        ),
        migrations.AlterField(
            model_name='centerwarehousingfile',
            name='file',
            field=models.FileField(upload_to='upload/center_library/2022/9/27', verbose_name='(采购计划、政府采购批复、投标手续)'),
        ),
    ]
