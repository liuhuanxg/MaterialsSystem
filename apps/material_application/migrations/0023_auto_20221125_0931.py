# Generated by Django 3.2 on 2022-11-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_application', '0022_alter_exapplicationfile_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationdetail',
            name='des',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='centerassessmentdetail',
            name='des',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='localassessmentdetail',
            name='des',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='exapplicationfile',
            name='file',
            field=models.FileField(upload_to='upload/center_library/2022/11/25', verbose_name='申请资料'),
        ),
        migrations.AlterField(
            model_name='exwarehousingapplication',
            name='applicant_phone',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='领用人手机号'),
        ),
    ]