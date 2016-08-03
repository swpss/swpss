# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0003_auto_20150705_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machine',
            old_name='machine_model',
            new_name='model',
        ),
    ]
