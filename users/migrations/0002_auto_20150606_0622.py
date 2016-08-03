# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(help_text=b'Enter the phone number WITHOUT country code', unique=True, max_length=10),
            preserve_default=True,
        ),
    ]
