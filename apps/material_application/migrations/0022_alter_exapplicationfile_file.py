# Generated by Django 3.2 on 2022-09-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_application', '0021_alter_accounts_specifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exapplicationfile',
            name='file',
            field=models.FileField(upload_to='upload/center_library/2022/9/29', verbose_name='申请资料'),
        ),
    ]
