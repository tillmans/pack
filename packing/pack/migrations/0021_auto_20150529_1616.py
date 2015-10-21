# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0020_auto_20150527_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='thirdChargeNO',
            field=models.CharField(default=b'0', max_length=40, verbose_name=b'\xe7\xac\xac\xe4\xb8\x89\xe6\x96\xb9\xe4\xba\xa4\xe6\x98\x93id'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 29, 16, 16, 8, 247000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='payStyle',
            field=models.CharField(default=b'F', max_length=1, verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98\xe6\x96\xb9\xe5\xbc\x8f', choices=[('N', 'online'), ('F', 'offline')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'TBST', max_length=4, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[('TBPD', b'toBePayed'), ('TBST', b'toBeSent'), ('TBUC', b'toBeUserConfirmed'), ('TBSC', b'toBeSalerConfirmed'), ('TBCM', b'toBeCommented'), ('FND', b'finished'), ('CCD', b'canceled'), ('IVD', b'invalid'), ('TBF', b'toBeRefunded'), ('RFD', b'refunded')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsaler',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 29, 16, 16, 8, 248000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 29, 16, 16, 8, 248000), verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', auto_now=True),
            preserve_default=True,
        ),
    ]
