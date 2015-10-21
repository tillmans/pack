# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0064_auto_20150908_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tableId',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'\xe9\xa4\x90\xe6\xa1\x8cid'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ordersku',
            name='status',
            field=models.CharField(default=b'0', max_length=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='table',
            name='peopleNumber',
            field=models.PositiveSmallIntegerField(default=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 1, 15, 19, 15, 129000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 1, 15, 19, 15, 129000), verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 1, 15, 19, 15, 129000), verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='officialmsg',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 1, 15, 19, 15, 129000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 1, 15, 19, 15, 129000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'TBST', max_length=4, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[('0', b'\xe5\xbe\x85\xe6\x94\xaf\xe4\xbb\x98'), ('1', b'\xe5\xbe\x85\xe5\x95\x86\xe5\xae\xb6\xe7\xa1\xae\xe8\xae\xa4'), ('3', b'\xe5\xbe\x85\xe7\xbb\x93\xe6\x9d\x9f'), ('4', b'\xe5\xbe\x85\xe6\xb8\x85\xe5\x8f\xb0'), ('5', b'\xe5\xbe\x85\xe8\xaf\x84\xe4\xbb\xb7'), ('6', b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90'), ('100', b'\xe5\x8f\x96\xe6\xb6\x88'), ('101', b'\xe5\xb7\xb2\xe5\xa4\xb1\xe6\x95\x88'), ('102', b'\xe9\x80\x80\xe6\xac\xbe\xe4\xb8\xad'), ('103', b'\xe5\xb7\xb2\xe9\x80\x80\xe6\xac\xbe')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 1, 15, 19, 15, 129000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 1, 15, 19, 15, 129000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 1, 15, 19, 15, 129000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salerevaluate',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 1, 15, 19, 15, 129000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
    ]
