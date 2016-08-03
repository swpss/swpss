# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0002_remove_machine_registered_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machine',
            old_name='model',
            new_name='machine_model',
        ),
    ]
