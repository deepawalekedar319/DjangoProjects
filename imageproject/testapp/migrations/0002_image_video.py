# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-10-11 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='video',
            field=models.FileField(default=None, upload_to='images'),
        ),
    ]