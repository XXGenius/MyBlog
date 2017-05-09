# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20170507_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название каегории')),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='article.Category'),
            preserve_default=False,
        ),
    ]