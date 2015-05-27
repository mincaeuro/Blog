# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20150520_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='kometar',
            name='postRef',
            field=models.ForeignKey(default=uuid.uuid4, to='posts.Prispevok', unique=True),
        ),
        migrations.AlterField(
            model_name='prispevok',
            name='hodnotenie',
            field=models.CharField(max_length=1),
        ),
    ]
