# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0005_auto_20150829_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='imsi_number',
            field=models.CharField(unique=True, max_length=15),
        ),
    ]
