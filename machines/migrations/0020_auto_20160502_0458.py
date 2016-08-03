# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0019_auto_20160502_0457'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinedetail',
            name='p_bee_rating',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='p_impeller',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='p_low_voltage',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='p_material',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='p_max_dynamic_head',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='p_no_of_stages',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='p_outlet_diameter',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='p_rated_head',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='p_rated_voltage',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
