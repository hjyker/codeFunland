# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userdockers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercode',
            options={'get_latest_by': 'created_time'},
        ),
        migrations.RemoveField(
            model_name='usercode',
            name='latest_time',
        ),
        migrations.AddField(
            model_name='usercode',
            name='code_path',
            field=models.TextField(default='test/a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usercode',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usercode',
            name='version',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdockers',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
