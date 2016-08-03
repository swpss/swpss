# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0009_auto_20160317_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinedetail',
            name='horse_power',
            field=models.FloatField(default=5),
        ),
    ]
