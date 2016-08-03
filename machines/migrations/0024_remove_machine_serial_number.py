# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0023_auto_20160504_0451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='serial_number',
        ),
    ]
