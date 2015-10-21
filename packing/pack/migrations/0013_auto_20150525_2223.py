# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0012_auto_20150525_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saler',
            old_name='realName',
            new_name='cardName',
        ),
    ]
