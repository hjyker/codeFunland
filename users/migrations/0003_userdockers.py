# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20150218_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDockers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docker_id', models.CharField(max_length=100)),
                ('docker_open_link', models.URLField()),
                ('docker_type', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'created_time',
            },
            bases=(models.Model,),
        ),
    ]
