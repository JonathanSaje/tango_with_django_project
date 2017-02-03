# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-03 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_auto_20170122_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
            ],
        ),
    ]
