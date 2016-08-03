# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0014_auto_20160421_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinedetail',
            name='con_model_no',
            field=models.CharField(default=1, unique=True, max_length=15),
            preserve_default=False,
        ),
    ]
