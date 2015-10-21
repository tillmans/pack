# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0002_auto_20150424_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='saler',
            name='sessionKey',
            field=models.CharField(default=b'', max_length=40),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='sessionKey',
            field=models.CharField(default=b'', max_length=40),
            preserve_default=True,
        ),
    ]
