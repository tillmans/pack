# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0033_auto_20150715_1600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='secondCategoryName',
            new_name='categoryName',
        ),
        migrations.RemoveField(
            model_name='category',
            name='firstCategory',
        ),
        migrations.DeleteModel(
            name='FirstCategory',
        ),
        migrations.RemoveField(
            model_name='sku',
            name='saler',
        ),
        migrations.AddField(
            model_name='category',
            name='saler',
            field=models.ForeignKey(default=1, to='pack.Saler'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 20, 21, 15, 19, 130000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 20, 21, 15, 19, 131000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 20, 21, 15, 19, 131000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
    ]
