# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-02 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('questionID', models.AutoField(primary_key=True, serialize=False)),
                ('Question', models.CharField(max_length=1000)),
                ('Answer', models.CharField(max_length=1000, null=True)),
                ('dateAsked', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-dateAsked'],
            },
        ),
    ]
