# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_auto_20170217_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(),
        ),
    ]
