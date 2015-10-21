# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0027_auto_20150601_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 11, 11, 58, 7, 564000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ordersku',
            name='number',
            field=models.PositiveSmallIntegerField(verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 11, 11, 58, 7, 566000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 11, 11, 58, 7, 565000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sku',
            name='salePrice',
            field=models.DecimalField(default=-1, verbose_name=b'\xe4\xbf\x83\xe9\x94\x80\xe5\x8d\x95\xe4\xbb\xb7', max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
    ]
