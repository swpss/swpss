# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0021_auto_20160502_0500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machinedetail',
            name='firmware',
        ),
        migrations.RemoveField(
            model_name='machinedetail',
            name='head_high',
        ),
        migrations.RemoveField(
            model_name='machinedetail',
            name='head_low',
        ),
        migrations.RemoveField(
            model_name='machinedetail',
            name='model_name',
        ),
        migrations.RemoveField(
            model_name='machinedetail',
            name='number_of_stages',
        ),
        migrations.RemoveField(
            model_name='machinedetail',
            name='optimal_depth',
        ),
        migrations.RemoveField(
            model_name='machinedetail',
            name='pump_rating',
        ),
        migrations.RemoveField(
            model_name='machinedetail',
            name='total_dynamic_head',
        ),
    ]
