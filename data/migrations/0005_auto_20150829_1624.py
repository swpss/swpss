# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20150829_1609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='imsi_number',
            new_name='gprs_imsi_number',
        ),
    ]
