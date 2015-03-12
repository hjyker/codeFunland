# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labs', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_content', models.TextField(null=True, blank=True)),
                ('latest_time', models.DateTimeField(default=datetime.datetime.now)),
                ('course_id', models.ForeignKey(to='courses.Courses')),
                ('lab_id', models.ForeignKey(to='labs.Labs')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docker_image', models.CharField(max_length=100, null=True, verbose_name='docker\u5bb9\u5668ID(\u957f)', blank=True)),
                ('avatar_link', models.ImageField(default=b'avatar/1.jpg', upload_to=b'avatar', verbose_name='\u5934\u50cf')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
