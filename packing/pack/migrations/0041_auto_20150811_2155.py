# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0040_auto_20150730_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 11, 21, 55, 30, 388000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 11, 21, 55, 30, 384000), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ordersku',
            name='skuId',
            field=models.CharField(default=b'1', max_length=20, verbose_name=b'skuId'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 11, 21, 55, 30, 391000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 11, 21, 55, 30, 390000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='headImage',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='nickName',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0'),
            preserve_default=True,
        ),
    ]
