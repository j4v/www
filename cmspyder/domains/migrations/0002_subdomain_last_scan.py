# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-15 07:24
from __future__ import unicode_literals

import django.utils.datetime_safe
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdomain',
            name='last_scan',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.datetime_safe.datetime.now),
            preserve_default=False,
        ),
    ]
