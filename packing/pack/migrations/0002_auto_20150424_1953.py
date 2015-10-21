# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saler',
            name='skuNumber',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saler',
            name='headImage',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saler',
            name='verifyBackImage',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='saler',
            name='verifyFrontImage',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
