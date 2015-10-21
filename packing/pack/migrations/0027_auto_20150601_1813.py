# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0026_auto_20150529_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 18, 13, 27, 99000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'TBST', max_length=4, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[('0', b'toBePayed'), ('1', b'toBeSent'), ('2', b'toBeUserConfirmed'), ('3', b'toBeSalerConfirmed'), ('4', b'toBeCommented'), ('5', b'finished'), ('100', b'canceled'), ('101', b'invalid'), ('102', b'toBeRefunded'), ('103', b'refunded')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 18, 13, 27, 99000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 1, 18, 13, 27, 99000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saler',
            name='basePrice',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'\xe8\xb5\xb7\xe9\x80\x81\xe4\xbb\xb7'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saler',
            name='salerType',
            field=models.CharField(max_length=1, verbose_name=b'\xe5\x95\x86\xe5\xae\xb6\xe7\xb1\xbb\xe5\x9e\x8b', choices=[('f', '\u6c34\u679c'), ('v', '\u852c\u83dc'), ('b', '\u65e9\u9910'), ('l', '\u5348\u665a\u9910'), ('o', '\u5176\u4ed6')]),
            preserve_default=True,
        ),
    ]
