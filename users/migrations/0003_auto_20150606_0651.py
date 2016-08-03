# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150606_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.IntegerField(choices=[(0, b'Supplier'), (1, b'Electricity Officer'), (2, b'Nodal Officer'), (3, b'Farmer'), (4, b'Manufacturer')]),
            preserve_default=True,
        ),
    ]
