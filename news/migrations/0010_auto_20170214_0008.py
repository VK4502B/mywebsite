# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 22:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20170213_1344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date', 'category']},
        ),
    ]
