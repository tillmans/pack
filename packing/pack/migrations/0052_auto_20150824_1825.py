# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0051_auto_20150824_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salerwallet',
            name='saler',
        ),
        migrations.DeleteModel(
            name='SalerWallet',
        ),
        migrations.AddField(
            model_name='saler',
            name='cardNumber',
            field=models.CharField(default=b'0', max_length=19, verbose_name=b'\xe5\x8d\xa1\xe5\x8f\xb7'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='saler',
            name='cardType',
            field=models.CharField(default=b'0', max_length=1, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b', choices=[('f', '\u5973'), ('m', '\u7537'), ('u', '\u672a\u77e5')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='saler',
            name='realName',
            field=models.CharField(default=b'0', max_length=20, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 18, 25, 46, 842000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 18, 25, 46, 842000), verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 18, 25, 46, 842000), verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='officialmsg',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 18, 25, 46, 842000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 18, 25, 46, 842000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 18, 25, 46, 842000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 18, 25, 46, 842000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 18, 25, 46, 842000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salerevaluate',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 18, 25, 46, 842000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
    ]
