# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-01 06:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20171201_0644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='questionAnswer',
            new_name='Answer',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='questionDescription',
            new_name='Description',
        ),
    ]
