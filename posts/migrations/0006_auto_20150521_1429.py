# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20150521_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kometar',
            name='postRef',
            field=models.ForeignKey(default=uuid.uuid4, to='posts.Prispevok'),
        ),
    ]
