# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0004_auto_20150511_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saler',
            name='telephone',
            field=models.CharField(unique=True, max_length=11),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(unique=True, max_length=11),
            preserve_default=True,
        ),
    ]
