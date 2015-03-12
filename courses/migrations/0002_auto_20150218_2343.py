# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labs', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='learnrecored',
            name='lab_id',
            field=models.ForeignKey(to='labs.Labs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='learnrecored',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courses',
            name='learn_recored_mtm',
            field=models.ManyToManyField(related_name=b'user_course_related', verbose_name=b'\xe5\xad\xa6\xe4\xb9\xa0\xe8\xae\xb0\xe5\xbd\x95', through='courses.LearnRecored', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courses',
            name='owner',
            field=models.ForeignKey(related_name=b'owner', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
