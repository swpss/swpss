# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0007_auto_20160317_0630'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='serial_number',
            field=models.IntegerField(null=True),
        ),
    ]
