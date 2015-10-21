# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0037_auto_20150720_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='saler',
            name='contactName',
            field=models.CharField(default=b'eep', max_length=50, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe5\x90\x8d\xe5\xad\x97'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='saler',
            name='whetherEatAtShop',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x94\xaf\xe6\x8c\x81\xe5\x88\xb0\xe5\xba\x97'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 16, 7, 7, 180000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 16, 7, 7, 182000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 16, 7, 7, 181000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saler',
            name='headImage',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\xba\x97\xe9\x93\xba\xe5\xa4\xb4\xe5\x83\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saler',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xba\x97\xe9\x93\xba\xe5\x90\x8d'),
            preserve_default=True,
        ),
    ]
