# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0047_auto_20150822_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalerWallet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cardName', models.CharField(default=b'0', max_length=20, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('cardNumber', models.CharField(default=b'0', max_length=19, verbose_name=b'\xe5\x8d\xa1\xe5\x8f\xb7')),
                ('cardType', models.CharField(default=b'0', max_length=1, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('saler', models.OneToOneField(to='pack.Saler')),
            ],
            options={
                'verbose_name': '\u5546\u5bb6\u94b1\u5305',
                'verbose_name_plural': '\u5546\u5bb6\u94b1\u5305\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='saler',
            name='everSetWallert',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xae\xbe\xe7\xbd\xae\xe8\xbf\x87\xe9\x92\xb1\xe5\x8c\x85'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 17, 29, 35, 848000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 17, 29, 35, 863000), verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 17, 29, 35, 863000), verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='officialmsg',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 17, 29, 35, 863000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 17, 29, 35, 848000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderrecord',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 17, 29, 35, 848000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 17, 29, 35, 863000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 17, 29, 35, 848000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salerevaluate',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 17, 29, 35, 848000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=True,
        ),
    ]
