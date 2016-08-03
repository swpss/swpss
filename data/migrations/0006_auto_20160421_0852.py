# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20150829_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='gprs_imsi_number',
            new_name='serial_no',
        ),
    ]
