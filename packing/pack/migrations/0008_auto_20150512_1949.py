# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0007_auto_20150512_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sessionKey',
        ),
        migrations.AddField(
            model_name='user',
            name='lastLoginTime',
            field=models.CharField(max_length=13, null=True, blank=True),
            preserve_default=True,
        ),
    ]
