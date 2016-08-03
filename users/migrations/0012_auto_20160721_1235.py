# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20160721_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techtype',
            name='client',
        ),
        migrations.RemoveField(
            model_name='techtype',
            name='technician',
        ),
        migrations.AddField(
            model_name='account',
            name='client',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='TechType',
        ),
    ]
