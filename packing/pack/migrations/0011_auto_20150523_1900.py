# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0010_auto_20150522_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saler',
            name='averageAttitudeLevel',
        ),
        migrations.RemoveField(
            model_name='saler',
            name='averageQualityLevel',
        ),
        migrations.RemoveField(
            model_name='saler',
            name='averageSpeedLevel',
        ),
        migrations.RemoveField(
            model_name='saler',
            name='orderNumber',
        ),
        migrations.RemoveField(
            model_name='saler',
            name='skuNumber',
        ),
    ]
