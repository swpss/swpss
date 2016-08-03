# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0006_auto_20150829_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='date_of_inspection',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='date_of_installation',
            field=models.DateField(null=True, blank=True),
        ),
    ]
