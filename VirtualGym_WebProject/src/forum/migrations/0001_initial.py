# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 06:03
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
            name='Questions',
            fields=[
                ('questionID', models.AutoField(primary_key=True, serialize=False)),
                ('questionDescription', models.CharField(max_length=1000)),
                ('dateAsked', models.DateTimeField(auto_now_add=True)),
                ('questionParent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Questions')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-dateAsked'],
            },
        ),
    ]
