# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0017_auto_20150526_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordersku',
            name='everConfirmed',
        ),
        migrations.RemoveField(
            model_name='ordersku',
            name='unit',
        ),
        migrations.AddField(
            model_name='ordersku',
            name='weight',
            field=models.CharField(default=b'0', max_length=10, verbose_name=b'\xe9\x87\x8d\xe9\x87\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 22, 53, 9, 951000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 22, 53, 9, 952000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 22, 53, 9, 952000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
    ]
