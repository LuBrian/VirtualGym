# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exerciseVideos',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]