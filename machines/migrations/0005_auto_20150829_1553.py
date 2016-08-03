# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0004_auto_20150705_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machine',
            old_name='phone_number',
            new_name='imsi_number',
        ),
    ]
