# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0008_machine_serial_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='serial_number',
            field=models.IntegerField(unique=True),
        ),
    ]
