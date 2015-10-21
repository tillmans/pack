# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('secondCategoryName', models.CharField(unique=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('money', models.PositiveSmallIntegerField()),
                ('startTime', models.DateTimeField(auto_now=True)),
                ('endTime', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FirstCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstCategoryName', models.CharField(unique=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OfficialMsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('msg', models.CharField(max_length=400)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('differSalerEvaluate', models.BooleanField(default=False)),
                ('sendStyle', models.CharField(default=b'S', max_length=1, choices=[('S', b'SENDING'), ('G', b'GET')])),
                ('priceTotal', models.DecimalField(max_digits=8, decimal_places=2)),
                ('payStyle', models.CharField(default=b'f', max_length=1, choices=[('N', 'online'), ('F', 'offline')])),
                ('status', models.CharField(default=b'TBCT', max_length=4, choices=[('TBCT', b'toBeCounted'), ('TBSN', b'toBeSend'), ('CCD', b'canceled'), ('TBCF', b'toBeConfirmed'), ('TBCM', b'toBeCommented'), ('FND', b'finished')])),
                ('memo', models.CharField(max_length=200)),
                ('timeStamp', models.BigIntegerField()),
                ('isValidToUser', models.BooleanField(default=True)),
                ('isValidToSaler', models.BooleanField(default=True)),
                ('unreadBySaler', models.BooleanField(default=True)),
                ('sendDay', models.CharField(max_length=8)),
                ('sendTimeStart', models.CharField(max_length=4)),
                ('sendTimeEnd', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderSKU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('unit', models.CharField(default=b'w', max_length=1, choices=[('w', 'weight'), ('b', 'bag')])),
                ('unitPrice', models.DecimalField(max_digits=8, decimal_places=2)),
                ('number', models.DecimalField(max_digits=8, decimal_places=2)),
                ('everConfirmed', models.BooleanField(default=False)),
                ('everEvaluated', models.BooleanField(default=False)),
                ('imgUrls', models.CharField(default=b'', max_length=300)),
                ('order', models.ForeignKey(to='pack.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReportSaler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(max_length=1, choices=[('CF', b'click farming'), ('PH', b'price too high')])),
                ('msg', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReportUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(max_length=1, choices=[('WA', b'wrong address'), ('BO', b'badly order'), ('OT', b'others')])),
                ('msg', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Saler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telephone', models.CharField(max_length=11)),
                ('everVerified2Saler', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(default=b'u', max_length=1, choices=[('f', 'female'), ('m', 'male'), ('u', 'unKnown')])),
                ('verifyFrontImage', models.CharField(max_length=50)),
                ('verifyBackImage', models.CharField(max_length=50)),
                ('headImage', models.CharField(max_length=50)),
                ('salerType', models.CharField(max_length=1, choices=[('f', 'fruit'), ('v', 'vegetable'), ('o', 'others')])),
                ('description', models.CharField(max_length=200)),
                ('isServiceOn', models.BooleanField(default=False)),
                ('accountLeft', models.DecimalField(default=0, max_digits=7, decimal_places=2)),
                ('moneyEarned', models.DecimalField(default=0, max_digits=7, decimal_places=2)),
                ('orderNumber', models.PositiveIntegerField(default=0)),
                ('serviceTime', models.CharField(max_length=60)),
                ('isVerified', models.BooleanField(default=False)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, geography=True, null=True, verbose_name='longitude/latitude', blank=True)),
                ('basePrice', models.PositiveSmallIntegerField(default=10)),
                ('averageAttitudeLevel', models.DecimalField(default=5, max_digits=3, decimal_places=2)),
                ('averageQualityLevel', models.DecimalField(default=5, max_digits=3, decimal_places=2)),
                ('averageSpeedLevel', models.DecimalField(default=5, max_digits=3, decimal_places=2)),
                ('level', models.PositiveSmallIntegerField(default=1)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('addressDetail', models.CharField(max_length=100)),
                ('clientID', models.CharField(default=b'000', max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SalerEvaluate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attitudeLevel', models.PositiveSmallIntegerField()),
                ('qualityLevel', models.PositiveSmallIntegerField()),
                ('speedLevel', models.PositiveSmallIntegerField()),
                ('comment', models.CharField(max_length=400)),
                ('imgUrls', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now=True)),
                ('saler', models.ForeignKey(to='pack.Saler')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=500)),
                ('oriPrice', models.DecimalField(max_digits=8, decimal_places=2)),
                ('salePrice', models.DecimalField(max_digits=8, decimal_places=2)),
                ('unit', models.CharField(default=b'w', max_length=1, choices=[('w', 'weight'), ('b', 'bag')])),
                ('stock', models.PositiveIntegerField(default=0)),
                ('averageQualityLevel', models.DecimalField(default=0, max_digits=3, decimal_places=2)),
                ('soldTotally', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('soldRecently', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('isOnSale', models.BooleanField(default=False)),
                ('isOnStock', models.BooleanField(default=True)),
                ('category', models.ForeignKey(to='pack.Category')),
                ('saler', models.ForeignKey(to='pack.Saler')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telephone', models.CharField(max_length=11)),
                ('nickName', models.CharField(max_length=50)),
                ('defaultAddressId', models.PositiveIntegerField(default=0)),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('score', models.PositiveSmallIntegerField(default=0)),
                ('accountBalance', models.DecimalField(default=0, max_digits=7, decimal_places=2)),
                ('headImage', models.CharField(max_length=50)),
                ('clientID', models.CharField(max_length=40)),
                ('likeSalers', models.ManyToManyField(to='pack.Saler')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('detail', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=11)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, geography=True, null=True, verbose_name='longitude/latitude', blank=True)),
                ('tag', models.CharField(default=b'N', max_length=1, choices=[('H', 'home'), ('S', 'school'), ('C', 'company'), ('N', 'none')])),
                ('user', models.ForeignKey(to='pack.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='salerevaluate',
            name='user',
            field=models.ForeignKey(to='pack.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reportuser',
            name='reportedUser',
            field=models.ForeignKey(to='pack.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reportuser',
            name='saler',
            field=models.ForeignKey(to='pack.Saler'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reportsaler',
            name='reportedSaler',
            field=models.ForeignKey(to='pack.Saler'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reportsaler',
            name='user',
            field=models.ForeignKey(to='pack.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ordersku',
            name='sku',
            field=models.ForeignKey(to='pack.SKU'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='saler',
            field=models.ForeignKey(to='pack.Saler'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='skuList',
            field=models.ManyToManyField(to='pack.SKU', through='pack.OrderSKU'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='pack.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coupon',
            name='user',
            field=models.ForeignKey(to='pack.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='firstCategory',
            field=models.ForeignKey(to='pack.FirstCategory'),
            preserve_default=True,
        ),
    ]
