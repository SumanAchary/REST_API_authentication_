# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 05:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180627_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_details',
            name='password',
        ),
        migrations.RemoveField(
            model_name='users_details',
            name='password',
        ),
    ]
