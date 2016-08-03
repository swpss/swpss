# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('machines', '0012_auto_20160322_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('isResolved', models.BooleanField(default=False)),
                ('serviceDate', models.DateField(null=True, blank=True)),
                ('solution', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('issue', models.ForeignKey(to='support.Issue')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('issue', models.ForeignKey(to='support.Issue')),
                ('reason', models.ForeignKey(to='support.Reason')),
            ],
        ),
        migrations.AddField(
            model_name='complaint',
            name='issue',
            field=models.ForeignKey(to='support.Issue'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='machine',
            field=models.ForeignKey(to='machines.Machine'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
