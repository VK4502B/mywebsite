# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20170217_1243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date', '-pub_time']},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='time_date',
            new_name='pub_time',
        ),
    ]