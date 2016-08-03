# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150606_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='location',
            field=models.CharField(default=b'IN-TG', max_length=5, choices=[(b'IN-PY', b'Puducherry'), (b'IN-KA', b'Karnataka'), (b'IN-BR', b'Bihar'), (b'IN-WB', b'West Bengal'), (b'IN-CT', b'Chhattisgarh'), (b'IN-TN', b'Tamil Nadu'), (b'IN-UT', b'Uttarakhand'), (b'IN-CH', b'Chandigarh'), (b'IN-AN', b'Andaman and Nicobar Island'), (b'IN-GA', b'Goa'), (b'IN-TG', b'Telangana'), (b'IN-SK', b'Sikkim'), (b'IN-GJ', b'Gujarat'), (b'IN-MN', b'Manipur'), (b'IN-DL', b'Delhi'), (b'IN-LD', b'Lakshadweep'), (b'IN-NL', b'Nagaland'), (b'IN-RJ', b'Rajasthan'), (b'IN-MP', b'Madhya Pradesh'), (b'IN-DN', b'Dadra and Nagar Haveli'), (b'IN-OR', b'Odisha'), (b'IN-HR', b'Haryana'), (b'IN-MZ', b'Mizoram'), (b'IN-HP', b'Himachal Pradesh'), (b'IN-AP', b'Andhra Pradesh'), (b'IN-TR', b'Tripura'), (b'IN-AR', b'Arunachal Pradesh'), (b'IN-AS', b'Assam'), (b'IN-DD', b'Daman and Diu'), (b'IN-PB', b'Punjab'), (b'IN-ML', b'Meghalaya'), (b'IN-JH', b'Jharkhand'), (b'IN-JK', b'Jammu and Kashmir'), (b'IN-UP', b'Uttar Pradesh'), (b'IN-MH', b'Maharashtra'), (b'IN-KL', b'Kerala')]),
            preserve_default=True,
        ),
    ]
