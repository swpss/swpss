# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 4, 9, 29, 45, 970321, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
