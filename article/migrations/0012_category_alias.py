# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-05 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20170508_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='alias',
            field=models.SlugField(default=1, verbose_name='Alias категории'),
            preserve_default=False,
        ),
    ]
