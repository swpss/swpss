# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0004_auto_20150705_1341'),
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='machine',
            field=models.ForeignKey(default=1, to='machines.Machine'),
            preserve_default=False,
        ),
    ]
