# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-22 16:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170121_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2017, 1, 22, 16, 17, 7, 54851, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
