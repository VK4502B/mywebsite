# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170208_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='10', max_length=40),
        ),
    ]
