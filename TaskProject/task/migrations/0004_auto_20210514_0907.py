# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-05-14 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20210513_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='id',
        ),
        migrations.AddField(
            model_name='comments',
            name='sno',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]