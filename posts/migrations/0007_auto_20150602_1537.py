# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20150521_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.TextField(max_length=3000)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('user', models.CharField(max_length=50)),
                ('postRef', models.ForeignKey(default=uuid.uuid4, to='posts.Prispevok')),
            ],
        ),
        migrations.RemoveField(
            model_name='kometar',
            name='postRef',
        ),
        migrations.DeleteModel(
            name='kometar',
        ),
    ]
