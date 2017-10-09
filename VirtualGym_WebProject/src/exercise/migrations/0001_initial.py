# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 03:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('exerciseId', models.AutoField(primary_key=True, serialize=False)),
                ('exerciseDescription', models.CharField(max_length=500)),
                ('exerciseTag', models.CharField(max_length=50)),
                ('exerciseData', models.DateTimeField(auto_now_add=True)),
                ('exerciseVideos', models.FileField(max_length=500, upload_to=b'./uploadVideo/')),
                ('exercisePosterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
