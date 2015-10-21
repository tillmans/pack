# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0068_auto_20151005_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='saler',
            name='isEatWithoutTableValid',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\xaf\xe4\xbb\xa5\xe5\xba\x97\xe5\x86\x85\xe6\x97\xa0\xe6\xa1\x8c\xe7\x82\xb9\xe9\xa4\x90'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='saler',
            name='isTakenValid',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\xaf\xe4\xbb\xa5\xe6\x89\x93\xe5\x8c\x85'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='table',
            name='lockTimeStamp',
            field=models.CharField(default=b'0', max_length=b'20', verbose_name=b'\xe9\x94\x81\xe5\xae\x9a\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xb3'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='table',
            name='userId',
            field=models.CharField(default=b'0', max_length=20, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7id'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 10, 9, 24, 632000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 10, 9, 24, 632000), verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 10, 9, 24, 632000), verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='officialmsg',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 10, 9, 24, 632000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 10, 9, 24, 617000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='eatStyle',
            field=models.CharField(default=b'0', max_length=1, verbose_name=b'\xe9\x85\x8d\xe9\x80\x81\xe6\x96\xb9\xe5\xbc\x8f', choices=[('0', '\u6253\u5305\u5e26\u8d70'), ('1', '\u5e97\u5185\u684c\u53f7\u7528\u9910'), ('2', '\u5e97\u5185\u65e0\u684c\u53f7\u7528\u9910')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 10, 9, 24, 617000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 10, 9, 24, 632000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 10, 9, 24, 632000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salerevaluate',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 13, 10, 9, 24, 617000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='table',
            name='number',
            field=models.CharField(max_length=100, verbose_name=b'\xe4\xba\xba\xe6\x95\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='table',
            name='status',
            field=models.CharField(default=b'0', max_length=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[('0', '\u7a7a\u95f2'), ('1', '\u5fd9\u788c'), ('2', '\u9501\u5b9a'), ('200', '\u4e0d\u5bf9\u5916\u5f00\u653e')]),
            preserve_default=True,
        ),
    ]
