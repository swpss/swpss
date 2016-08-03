# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20160404_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.IntegerField()),
                ('Technician', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
