# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170420_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='time_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
