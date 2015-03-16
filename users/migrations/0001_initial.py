# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0005_auto_20150306_0101'),
        ('labs', '0004_auto_20150306_0101'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_path', models.TextField()),
                ('code_content', models.TextField(null=True, blank=True)),
                ('version', models.IntegerField(default=1)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(to='courses.Courses')),
                ('lab', models.ForeignKey(to='labs.Labs')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'created_time',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserDockers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docker_id', models.CharField(max_length=100)),
                ('docker_open_link', models.URLField()),
                ('docker_type', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'created_time',
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
