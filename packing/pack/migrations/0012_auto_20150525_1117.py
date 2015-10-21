# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pack', '0011_auto_20150523_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acount', models.DecimalField(verbose_name=b'\xe5\x8d\x95\xe4\xbb\xb7', max_digits=8, decimal_places=2)),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('status', models.CharField(default=b'C', max_length=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[('C', b'check'), ('D', b'doing'), ('F', b'finished')])),
                ('saler', models.ForeignKey(to='pack.Saler')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='sku',
            name='isOnSale',
        ),
        migrations.RemoveField(
            model_name='sku',
            name='soldRecently',
        ),
        migrations.RemoveField(
            model_name='sku',
            name='soldTotally',
        ),
        migrations.AddField(
            model_name='saler',
            name='cardNumber',
            field=models.CharField(default=b'0', max_length=19, verbose_name=b'\xe5\x8d\xa1\xe5\x8f\xb7'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='saler',
            name='realName',
            field=models.CharField(default=b'0', max_length=20, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97'),
            preserve_default=True,
        ),
    ]
