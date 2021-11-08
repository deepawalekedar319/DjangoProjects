# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-10-11 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_image_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(default='SOME STRING', upload_to='videos/%y')),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='video',
        ),
    ]