# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20170807_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='started',
            field=models.DateTimeField(),
        ),
    ]