# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20150218_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learnrecored',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='learnrecored',
            old_name='lab_id',
            new_name='lab',
        ),
        migrations.RenameField(
            model_name='learnrecored',
            old_name='user_id',
            new_name='user',
        ),
    ]
