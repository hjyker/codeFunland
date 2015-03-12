# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0002_auto_20150218_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='labs',
            name='weight',
            field=models.IntegerField(default=1, verbose_name='weight'),
            preserve_default=False,
        ),
    ]
