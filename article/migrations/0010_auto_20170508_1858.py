# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20170508_1841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Характеристика', 'verbose_name_plural': 'Характеристики'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='title',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=11, max_length=20, verbose_name='Название категории'),
            preserve_default=False,
        ),
    ]
