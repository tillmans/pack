# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0018_auto_20150526_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 11, 34, 13, 941000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'TBSN', max_length=4, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[('TBSN', b'toBeSend'), ('CCD', b'canceled'), ('TBCF', b'toBeConfirmed'), ('TBCM', b'toBeCommented'), ('FND', b'finished')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 11, 34, 13, 943000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 11, 34, 13, 942000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
    ]
