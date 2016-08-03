# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(unique=True, max_length=10)),
                ('latitude', models.DecimalField(null=True, max_digits=8, decimal_places=5, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=8, decimal_places=5, blank=True)),
                ('location', models.CharField(max_length=5, choices=[(b'IN-PY', b'Puducherry'), (b'IN-KA', b'Karnataka'), (b'IN-BR', b'Bihar'), (b'IN-WB', b'West Bengal'), (b'IN-CT', b'Chhattisgarh'), (b'IN-TN', b'Tamil Nadu'), (b'IN-UT', b'Uttarakhand'), (b'IN-CH', b'Chandigarh'), (b'IN-AN', b'Andaman and Nicobar Island'), (b'IN-GA', b'Goa'), (b'IN-TG', b'Telangana'), (b'IN-SK', b'Sikkim'), (b'IN-GJ', b'Gujarat'), (b'IN-MN', b'Manipur'), (b'IN-DL', b'Delhi'), (b'IN-LD', b'Lakshadweep'), (b'IN-NL', b'Nagaland'), (b'IN-RJ', b'Rajasthan'), (b'IN-MP', b'Madhya Pradesh'), (b'IN-DN', b'Dadra and Nagar Haveli'), (b'IN-OR', b'Odisha'), (b'IN-HR', b'Haryana'), (b'IN-MZ', b'Mizoram'), (b'IN-HP', b'Himachal Pradesh'), (b'IN-AP', b'Andhra Pradesh'), (b'IN-TR', b'Tripura'), (b'IN-AR', b'Arunachal Pradesh'), (b'IN-AS', b'Assam'), (b'IN-DD', b'Daman and Diu'), (b'IN-PB', b'Punjab'), (b'IN-ML', b'Meghalaya'), (b'IN-JH', b'Jharkhand'), (b'IN-JK', b'Jammu and Kashmir'), (b'IN-UP', b'Uttar Pradesh'), (b'IN-MH', b'Maharashtra'), (b'IN-KL', b'Kerala')])),
                ('depth_during_installation', models.FloatField(null=True)),
                ('date_of_installation', models.DateTimeField(null=True, blank=True)),
                ('date_of_inspection', models.DateTimeField(null=True, blank=True)),
                ('bought_by', models.ForeignKey(related_name='farmer', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MachineDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firmware', models.CharField(max_length=15)),
                ('rating_watts', models.FloatField()),
                ('rating_volts', models.FloatField()),
                ('rpm', models.FloatField()),
                ('rating_low_volts', models.FloatField()),
                ('rating_high_volts', models.FloatField()),
                ('make', models.CharField(max_length=15)),
                ('model', models.CharField(max_length=15)),
                ('year', models.IntegerField()),
                ('head_low', models.FloatField()),
                ('head_high', models.FloatField()),
                ('number_of_stages', models.FloatField()),
                ('pump_rating', models.FloatField()),
                ('model_name', models.CharField(max_length=15)),
                ('optimal_depth', models.FloatField()),
                ('total_dynamic_head', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='machine',
            name='model',
            field=models.ForeignKey(related_name='machine_detail', to='machines.MachineDetail'),
        ),
        migrations.AddField(
            model_name='machine',
            name='registered_by',
            field=models.ForeignKey(related_name='manufacturer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='machine',
            name='sold_by',
            field=models.ForeignKey(related_name='supplier', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
