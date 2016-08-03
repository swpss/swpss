# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0011_auto_20160322_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machinedetail',
            old_name='ref_hed_lpm',
            new_name='ref_head_lpm',
        ),
    ]
