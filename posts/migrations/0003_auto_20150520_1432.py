# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20150520_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kometar',
            name='text',
            field=models.TextField(max_length=3000),
        ),
    ]
