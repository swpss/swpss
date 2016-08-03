# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0015_machinedetail_con_model_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinedetail',
            name='con_enclosure_version',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='con_firmware_version',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='con_hardware_version',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='con_serial_no',
            field=models.CharField(default=1, unique=True, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='con_year',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]
