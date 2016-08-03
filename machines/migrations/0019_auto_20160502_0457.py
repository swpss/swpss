# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0018_auto_20160502_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinedetail',
            name='p_head_high',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='p_head_low',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='p_make',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='p_model',
            field=models.CharField(default=1, unique=True, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='p_rpm',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='machinedetail',
            name='p_year',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]
