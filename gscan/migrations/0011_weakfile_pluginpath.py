# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gscan', '0010_auto_20160428_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='weakfile',
            name='pluginpath',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]