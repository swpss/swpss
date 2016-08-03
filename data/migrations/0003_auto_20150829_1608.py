# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_dataset_machine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='gprs_phone_number',
            new_name='imsi_number',
        ),
    ]
