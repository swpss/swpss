# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0024_remove_machine_serial_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machinedetail',
            name='con_serial_no',
        ),
        migrations.AddField(
            model_name='machine',
            name='serial_number',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
