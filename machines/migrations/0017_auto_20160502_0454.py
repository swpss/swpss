# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0016_auto_20160502_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinedetail',
            name='con_certifications',
            field=models.CharField(default=b'UL', max_length=4, choices=[(b'IPV5', b'IPV5'), (b'TUV', b'TUV'), (b'VEC', b'VEC'), (b'UL', b'UL')]),
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='con_drive_capacity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='con_max_input_current',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='con_mppt_max_volts',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='con_mppt_min_volts',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='con_open_circuit_voltage',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
