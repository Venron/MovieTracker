# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20170807_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='started',
            field=models.DateTimeField(auto_now=True),
        ),
    ]