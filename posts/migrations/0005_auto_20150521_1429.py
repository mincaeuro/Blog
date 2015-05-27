# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20150521_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kometar',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='prispevok',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
