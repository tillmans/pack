# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0003_auto_20150511_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportsaler',
            name='reason',
            field=models.CharField(max_length=2, choices=[('CF', b'click farming'), ('PH', b'price too high')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportuser',
            name='reason',
            field=models.CharField(max_length=2, choices=[('WA', b'wrong address'), ('BO', b'badly order'), ('OT', b'others')]),
            preserve_default=True,
        ),
    ]
