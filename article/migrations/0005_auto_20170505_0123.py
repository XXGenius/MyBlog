# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20170313_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_img',
            field=models.ImageField(default=2, upload_to='', verbose_name='Картинка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]
