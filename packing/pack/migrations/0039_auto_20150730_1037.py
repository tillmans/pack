# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0038_auto_20150722_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record', models.CharField(max_length=200, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('date', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(to='pack.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='differSalerEvaluate',
        ),
        migrations.RemoveField(
            model_name='order',
            name='sendDay',
        ),
        migrations.RemoveField(
            model_name='order',
            name='sendStyle',
        ),
        migrations.RemoveField(
            model_name='order',
            name='sendTimeEnd',
        ),
        migrations.RemoveField(
            model_name='order',
            name='sendTimeStart',
        ),
        migrations.RemoveField(
            model_name='order',
            name='skuList',
        ),
        migrations.RemoveField(
            model_name='order',
            name='timeStamp',
        ),
        migrations.RemoveField(
            model_name='ordersku',
            name='everEvaluated',
        ),
        migrations.RemoveField(
            model_name='ordersku',
            name='imgUrls',
        ),
        migrations.RemoveField(
            model_name='ordersku',
            name='sku',
        ),
        migrations.RemoveField(
            model_name='saler',
            name='basePrice',
        ),
        migrations.RemoveField(
            model_name='saler',
            name='cardName',
        ),
        migrations.RemoveField(
            model_name='saler',
            name='cardNumber',
        ),
        migrations.RemoveField(
            model_name='saler',
            name='everVerified2Saler',
        ),
        migrations.RemoveField(
            model_name='sku',
            name='averageQualityLevel',
        ),
        migrations.RemoveField(
            model_name='sku',
            name='isOnStock',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 30, 10, 36, 54, 678000), auto_now=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='eatStyle',
            field=models.CharField(default=b'0', max_length=1, verbose_name=b'\xe9\x85\x8d\xe9\x80\x81\xe6\x96\xb9\xe5\xbc\x8f', choices=[('0', b'\xe6\x89\x93\xe5\x8c\x85\xe5\xb8\xa6\xe8\xb5\xb0'), ('1', b'\xe5\xba\x97\xe5\x86\x85\xe7\x94\xa8\xe9\xa4\x90')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ordersku',
            name='skuId',
            field=models.CharField(default=1, max_length=20, verbose_name=b'skuId'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saler',
            name='everSetSalerInfo',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xae\xbe\xe7\xbd\xae\xe8\xbf\x87\xe5\x95\x86\xe5\xae\xb6\xe4\xbf\xa1\xe6\x81\xaf'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sku',
            name='isValid',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe6\x95\x88'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 30, 10, 36, 54, 680000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='isValidToSaler',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xaf\xb9\xe5\x95\x86\xe5\xae\xb6\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe6\x95\x88'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='isValidToUser',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\xaf\xb9\xe7\x94\xa8\xe6\x88\xb7\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe6\x95\x88'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='payStyle',
            field=models.CharField(default=b'0', max_length=1, verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98\xe6\x96\xb9\xe5\xbc\x8f', choices=[('0', '\u652f\u4ed8\u5b9d\u4ed8\u6b3e'), ('1', '\u5fae\u4fe1\u4ed8\u6b3e')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'TBST', max_length=4, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[('0', b'\xe5\xbe\x85\xe6\x94\xaf\xe4\xbb\x98'), ('1', b'\xe5\xbe\x85\xe5\xa4\x84\xe7\x90\x86'), ('3', b'\xe5\xbe\x85\xe7\xa1\xae\xe8\xae\xa4'), ('4', b'\xe5\xbe\x85\xe8\xaf\x84\xe8\xae\xba'), ('5', b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90'), ('100', b'\xe5\x8f\x96\xe6\xb6\x88'), ('101', b'\xe5\xb7\xb2\xe5\xa4\xb1\xe6\x95\x88'), ('102', b'\xe9\x80\x80\xe6\xac\xbe\xe4\xb8\xad'), ('103', b'\xe5\xb7\xb2\xe9\x80\x80\xe6\xac\xbe')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ordersku',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'SKU\xe5\x90\x8d\xe5\xad\x97'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ordersku',
            name='weightInfo',
            field=models.CharField(default=b'0', max_length=10, verbose_name=b'\xe9\x87\x8d\xe9\x87\x8f\xe4\xbf\xa1\xe6\x81\xaf'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 30, 10, 36, 54, 681000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 30, 10, 36, 54, 681000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saler',
            name='isServiceOn',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x9c\xa8\xe7\xba\xbf\xe6\x9c\x8d\xe5\x8a\xa1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saler',
            name='salerType',
            field=models.CharField(default=b'0', max_length=2, verbose_name=b'\xe5\x95\x86\xe5\xae\xb6\xe7\xb1\xbb\xe5\x9e\x8b', choices=[('0', '\u679c\u852c'), ('1', '\u5c0f\u5403'), ('2', '\u5feb\u9910'), ('100', '\u5176\u4ed6')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saler',
            name='sex',
            field=models.CharField(default=b'u', max_length=1, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[('f', '\u5973'), ('m', '\u7537'), ('u', '\u672a\u77e5')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saler',
            name='verifyStatus',
            field=models.CharField(default=b'0', max_length=1, choices=[('0', '\u672a\u5ba1\u6838'), ('1', '\u5ba1\u6838\u672a\u901a\u8fc7'), ('2', '\u5ba1\u6838\u901a\u8fc7'), ('3', '\u5ba1\u6838\u4e2d')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sku',
            name='oriPrice',
            field=models.DecimalField(default=1, verbose_name=b'\xe5\x8d\x95\xe4\xbb\xb7', max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sku',
            name='salePrice',
            field=models.DecimalField(default=0, verbose_name=b'\xe4\xbf\x83\xe9\x94\x80\xe5\x8d\x95\xe4\xbb\xb7', max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
    ]
