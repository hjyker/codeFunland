# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60, verbose_name='\u5b9e\u9a8c\u540d\u79f0')),
                ('description', models.CharField(max_length=300, null=True, verbose_name='\u5b9e\u9a8c\u63cf\u8ff0', blank=True)),
                ('docker_image', models.URLField(max_length=300, null=True, verbose_name='docker \u5bb9\u5668', blank=True)),
                ('views', models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u4eba\u6570', blank=True)),
                ('document_link', models.URLField(max_length=300, null=True, verbose_name='\u5b9e\u9a8c\u6587\u6863', blank=True)),
                ('created_time', models.DateTimeField(default=datetime.datetime.now)),
                ('course_id', models.ForeignKey(to='courses.Courses')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
