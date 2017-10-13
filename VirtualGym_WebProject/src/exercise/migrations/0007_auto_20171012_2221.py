# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0006_auto_20171012_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='exerciseApproved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='exercise',
            name='exerciseQuestions',
            field=models.ManyToManyField(through='exercise.QuestionsExercises', to='exercise.Questions'),
        ),
    ]
