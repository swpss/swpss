# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160322_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.IntegerField(choices=[(0, b'Supplier'), (1, b'Electricity Officer'), (2, b'Nodal Officer'), (3, b'Farmer'), (4, b'Manufacturer'), (5, b'Technician')]),
        ),
    ]
