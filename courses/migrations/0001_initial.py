# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60, verbose_name='\u8bfe\u7a0b\u540d')),
                ('label', models.IntegerField(default=0, verbose_name='\u8bfe\u7a0b\u6807\u7b7e')),
                ('image', models.ImageField(default=b'avatar/1.jpg', upload_to=b'avatar', verbose_name='\u8bfe\u7a0b\u56fe\u7247')),
                ('description', models.CharField(max_length=300, null=True, verbose_name='\u8bfe\u7a0b\u63cf\u8ff0', blank=True)),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('views', models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u4eba\u6570', blank=True)),
                ('likes', models.IntegerField(default=0, verbose_name='\u5173\u6ce8\u4eba\u6570', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LearnRecored',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latest_time', models.DateTimeField(default=datetime.datetime.now)),
                ('course_id', models.ForeignKey(to='courses.Courses')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
