# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0039_auto_20150730_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 30, 15, 23, 47, 153000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 30, 15, 23, 47, 149000), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 30, 15, 23, 47, 154000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 30, 15, 23, 47, 153000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
    ]
