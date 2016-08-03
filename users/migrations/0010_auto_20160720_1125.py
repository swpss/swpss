# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_techtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techtype',
            name='Technician',
        ),
        migrations.AddField(
            model_name='techtype',
            name='technician',
            field=models.ForeignKey(related_name='technician', default=0, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='techtype',
            name='client',
            field=models.ForeignKey(related_name='client', default=0, to=settings.AUTH_USER_MODEL),
        ),
    ]
