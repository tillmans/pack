# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0009_auto_20150521_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='skuInfo',
            field=models.CharField(default=b'0', max_length=100, verbose_name=b'sku\xe4\xbf\xa1\xe6\x81\xaf'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='lastLoginTime',
            field=models.CharField(default=b'0', max_length=13, verbose_name=b'\xe4\xb8\x8a\xe6\xac\xa1\xe7\x99\xbb\xe5\xbd\x95\xe6\x97\xb6\xe9\x97\xb4'),
            preserve_default=True,
        ),
    ]
