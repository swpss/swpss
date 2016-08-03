# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gprs_phone_number', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('data', django_hstore.fields.SerializedDictionaryField()),
            ],
        ),
    ]
