# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0042_auto_20150812_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 18, 16, 36, 32, 668000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 18, 16, 36, 32, 665000), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 18, 16, 36, 32, 669000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 18, 16, 36, 32, 669000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saler',
            name='salerType',
            field=models.CharField(default=b'0', max_length=2, verbose_name=b'\xe5\x95\x86\xe5\xae\xb6\xe7\xb1\xbb\xe5\x9e\x8b', choices=[('0', '\u5feb\u9910'), ('1', '\u679c\u852c'), ('2', '\u5c0f\u5403'), ('100', '\u5176\u4ed6')]),
            preserve_default=True,
        ),
    ]
