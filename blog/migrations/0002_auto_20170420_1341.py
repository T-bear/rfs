# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 11:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='auth_user_id',
            new_name='auth_user',
        ),
    ]