# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import exercise.models


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
                ('exerciseDescription', models.CharField(max_length=5000)),
                ('exerciseDate', models.DateTimeField(auto_now_add=True)),
                ('exerciseApproved', models.BooleanField(default=False)),
                ('exerciseName', models.CharField(max_length=1000)),
                ('exercisePosterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('tagID', models.AutoField(primary_key=True, serialize=False)),
                ('tagDescription', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TagsExercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.Exercise')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('annotations', models.CharField(max_length=5000)),
                ('videoFile', models.FileField(upload_to=exercise.models.upload_location)),
                ('exercisePosterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VideosExercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.Exercise')),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.Videos')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='exerciseTag',
            field=models.ManyToManyField(through='exercise.TagsExercises', to='exercise.Tags'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='exerciseVideos',
            field=models.ManyToManyField(through='exercise.VideosExercises', to='exercise.Videos'),
        ),
    ]
