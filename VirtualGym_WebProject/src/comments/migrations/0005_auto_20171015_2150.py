# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 21:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20171014_0133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-CommentTimestamp']},
        ),
    ]
