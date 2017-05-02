# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170420_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='blog_post',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='time_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
