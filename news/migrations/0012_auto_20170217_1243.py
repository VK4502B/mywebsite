# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20170214_0008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date', '-time_date']},
        ),
        migrations.AddField(
            model_name='article',
            name='time_date',
            field=models.TimeField(default='00:00'),
        ),
    ]