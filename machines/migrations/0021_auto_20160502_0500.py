# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0020_auto_20160502_0458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machinedetail',
            name='make',
        ),
        migrations.RemoveField(
            model_name='machinedetail',
            name='model',
        ),
        migrations.RemoveField(
            model_name='machinedetail',
            name='rating_high_volts',
        ),
        migrations.RemoveField(
            model_name='machinedetail',
            name='rating_low_volts',
        ),
        migrations.RemoveField(
            model_name='machinedetail',
            name='rating_volts',
        ),
        migrations.RemoveField(
            model_name='machinedetail',
            name='rating_watts',
        ),
        migrations.RemoveField(
            model_name='machinedetail',
            name='rpm',
        ),
        migrations.RemoveField(
            model_name='machinedetail',
            name='year',
        ),
    ]
