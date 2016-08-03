# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0013_machine_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machine',
            old_name='imsi_number',
            new_name='m_id',
        ),
    ]
