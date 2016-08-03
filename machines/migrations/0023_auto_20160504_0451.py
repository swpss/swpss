# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0022_auto_20160502_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinedetail',
            name='con_model_no',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='machinedetail',
            name='con_serial_no',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='machinedetail',
            name='p_model',
            field=models.CharField(max_length=15),
        ),
    ]
