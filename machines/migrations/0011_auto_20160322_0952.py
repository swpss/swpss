# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0010_machinedetail_horse_power'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinedetail',
            name='pump_type',
            field=models.CharField(default=b'SMB', max_length=3, choices=[(b'SMB', b'Submersible')]),
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='ref_head',
            field=models.FloatField(default=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='ref_hed_lpm',
            field=models.FloatField(default=160),
            preserve_default=False,
        ),
    ]
