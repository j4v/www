# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 19:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0007_subdomain_discovered_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subdomain',
            name='discovered_by',
        ),
    ]
