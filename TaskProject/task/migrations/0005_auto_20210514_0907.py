# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-05-14 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20210514_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='sno',
        ),
        migrations.AddField(
            model_name='comments',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10),
        ),
    ]
