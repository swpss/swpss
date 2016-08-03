# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0017_auto_20160502_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinedetail',
            name='con_max_frequency',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='con_max_output_current',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='con_output_voltage_range',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
