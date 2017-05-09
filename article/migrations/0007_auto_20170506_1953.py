# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-06 19:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0006_auto_20170505_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_likes',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_date',
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_img',
        ),
        migrations.RemoveField(
            model_name='article',
            name='user_article',
        ),
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата публикации'),
        ),
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='username_comments',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]