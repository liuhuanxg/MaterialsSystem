# Generated by Django 3.2 on 2022-09-03 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material_application', '0015_accounts_supplier_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='supplier_name',
            field=models.CharField(default='', max_length=100, verbose_name='供应商名称'),
        ),
    ]
