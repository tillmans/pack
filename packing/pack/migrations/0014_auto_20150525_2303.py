# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0013_auto_20150525_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='cardName',
            field=models.CharField(default=b'0', max_length=20, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bill',
            name='cardNumber',
            field=models.CharField(default=b'0', max_length=19, verbose_name=b'\xe5\x8d\xa1\xe5\x8f\xb7'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 23, 3, 34, 37000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 23, 3, 34, 36000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 23, 3, 34, 36000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
    ]
