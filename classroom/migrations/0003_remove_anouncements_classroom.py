# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 00:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_auto_20170521_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anouncements',
            name='classroom',
        ),
    ]
