# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0031_auto_20150714_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='saler',
            name='verifyStatus',
            field=models.CharField(default=b'1', max_length=1, choices=[('0', '\u672a\u901a\u8fc7'), ('1', '\u5ba1\u6838\u901a\u8fc7'), ('2', '\u5ba1\u6838\u4e2d')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 15, 16, 0, 1, 81000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 15, 16, 0, 1, 83000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 15, 16, 0, 1, 82000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
    ]
