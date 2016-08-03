# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150606_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 8, 18, 20, 917580, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 8, 18, 29, 797551, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
