# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0032_auto_20150715_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saler',
            name='isVerified',
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 15, 16, 0, 51, 466000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 15, 16, 0, 51, 475000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 15, 16, 0, 51, 473000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
    ]
