# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0059_auto_20150829_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrecord',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 29, 12, 13, 57, 798000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 29, 12, 13, 57, 800000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 29, 12, 13, 57, 804000), verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 29, 12, 13, 57, 804000), verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='officialmsg',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 29, 12, 13, 57, 804000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 29, 12, 13, 57, 796000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 29, 12, 13, 57, 798000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 29, 12, 13, 57, 802000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 29, 12, 13, 57, 801000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salerevaluate',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 29, 12, 13, 57, 799000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
    ]
