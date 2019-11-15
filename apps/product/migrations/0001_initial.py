# Generated by Django 2.2.7 on 2019-11-15 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('product_name', models.CharField(max_length=64, verbose_name='产品名称')),
                ('Product_desc', models.CharField(max_length=200, verbose_name='产品描述')),
                ('producter', models.CharField(max_length=200, verbose_name='产品负责人')),
            ],
            options={
                'verbose_name': '产品管理',
                'verbose_name_plural': '产品管理',
            },
        ),
    ]
