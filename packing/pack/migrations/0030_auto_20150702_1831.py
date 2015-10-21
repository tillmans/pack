# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0029_auto_20150622_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='telephone',
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 18, 31, 41, 879000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'TBST', max_length=4, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[('0', b'toBePayed'), ('1', b'toBePacked'), ('2', b'toBeUserConfirmed'), ('3', b'toBeSalerConfirmed'), ('4', b'toBeCommented'), ('5', b'finished'), ('100', b'canceled'), ('101', b'invalid'), ('102', b'toBeRefunded'), ('103', b'refunded')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 18, 31, 41, 881000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 18, 31, 41, 880000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salerfeedback',
            name='msg',
            field=models.CharField(max_length=400, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
            preserve_default=True,
        ),
    ]
