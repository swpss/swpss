# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0012_auto_20160322_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
    ]
