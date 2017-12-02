# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('CommentId', models.AutoField(primary_key=True, serialize=False)),
                ('CommentContent', models.TextField()),
                ('CommentTimestamp', models.DateTimeField(auto_now_add=True)),
                ('CommentExercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.Exercise')),
                ('CommentParent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.Comment')),
                ('CommentPoster', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-CommentTimestamp'],
            },
        ),
    ]
