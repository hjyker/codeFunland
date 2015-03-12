# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20150224_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='\u8bfe\u7a0b\u72b6\u6001'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courses',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='learnrecored',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
