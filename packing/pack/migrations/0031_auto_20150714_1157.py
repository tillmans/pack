# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0030_auto_20150702_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 11, 57, 2, 153000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 11, 57, 2, 153000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 11, 57, 2, 153000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saler',
            name='salerType',
            field=models.CharField(max_length=2, verbose_name=b'\xe5\x95\x86\xe5\xae\xb6\xe7\xb1\xbb\xe5\x9e\x8b', choices=[('f', '\u6c34\u679c'), ('v', '\u852c\u83dc'), ('fv', '\u679c\u852c\u7efc\u5408'), ('o', '\u5176\u4ed6')]),
            preserve_default=True,
        ),
    ]
