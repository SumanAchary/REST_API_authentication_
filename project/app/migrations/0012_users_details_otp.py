# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-30 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_delete_login_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_details',
            name='otp',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
