# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150218_2357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learnrecored',
            old_name='latest_time',
            new_name='created_time',
        ),
    ]
