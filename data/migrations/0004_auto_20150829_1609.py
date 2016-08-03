# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20150829_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='imsi_number',
            field=models.CharField(max_length=15),
        ),
    ]
