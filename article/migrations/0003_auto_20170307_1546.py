# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170307_1400'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='article',
            table='Article',
        ),
        migrations.AlterModelTable(
            name='comments',
            table='Comments',
        ),
    ]
