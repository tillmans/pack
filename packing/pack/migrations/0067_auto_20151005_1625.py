# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0066_auto_20151001_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 16, 25, 26, 216000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 16, 25, 26, 218000), verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 16, 25, 26, 218000), verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='officialmsg',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 16, 25, 26, 219000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 16, 25, 26, 210000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='eatStyle',
            field=models.CharField(default=b'0', max_length=1, verbose_name=b'\xe9\x85\x8d\xe9\x80\x81\xe6\x96\xb9\xe5\xbc\x8f', choices=[('0', '\u6253\u5305\u5e26\u8d70'), ('1', '\u5e97\u5185\u7528\u9910')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'0', max_length=4, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[('0', '\u5f85\u652f\u4ed8'), ('1', '\u5f85\u5546\u5bb6\u786e\u8ba4'), ('3', '\u5f85\u7ed3\u675f'), ('4', '\u5f85\u6e05\u53f0'), ('5', '\u5f85\u8bc4\u4ef7'), ('6', '\u5df2\u5b8c\u6210'), ('100', '\u53d6\u6d88'), ('101', '\u5df2\u5931\u6548'), ('102', '\u9000\u6b3e\u4e2d'), ('103', '\u5df2\u9000\u6b3e')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 16, 25, 26, 214000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 16, 25, 26, 217000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 16, 25, 26, 216000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salerevaluate',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 16, 25, 26, 215000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='table',
            name='peopleNumber',
            field=models.PositiveSmallIntegerField(default=2, verbose_name=b'\xe5\xae\xb9\xe7\xba\xb3\xe4\xba\xba\xe6\x95\xb0'),
            preserve_default=True,
        ),
    ]
