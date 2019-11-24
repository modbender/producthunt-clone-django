# Generated by Django 2.1.8 on 2019-05-22 08:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20190522_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='voter',
        ),
        migrations.RemoveField(
            model_name='product',
            name='votes',
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 22, 13, 50, 3, 933112)),
        ),
    ]
