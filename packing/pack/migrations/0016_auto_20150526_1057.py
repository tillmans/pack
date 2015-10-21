# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0015_auto_20150525_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='sku',
            name='weight',
            field=models.DecimalField(default=0, verbose_name=b'\xe9\x87\x8d\xe9\x87\x8f', max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 10, 57, 33, 207000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ordersku',
            name='unit',
            field=models.CharField(default=b'w', max_length=1, verbose_name=b'sku\xe5\x8d\x95\xe4\xbd\x8d', choices=[('n', 'none'), ('g', 'gram'), ('kg', 'kilogram')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 10, 57, 33, 208000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 10, 57, 33, 208000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sku',
            name='oriPrice',
            field=models.DecimalField(default=0, verbose_name=b'\xe5\x8d\x95\xe4\xbb\xb7', max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sku',
            name='salePrice',
            field=models.DecimalField(default=0, verbose_name=b'\xe4\xbf\x83\xe9\x94\x80\xe5\x8d\x95\xe4\xbb\xb7', max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sku',
            name='unit',
            field=models.CharField(default=b'n', max_length=2, verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d', choices=[('n', 'none'), ('g', 'gram'), ('kg', 'kilogram')]),
            preserve_default=True,
        ),
    ]
