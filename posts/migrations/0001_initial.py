# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import posts.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kometar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=3000)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('user', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prispevok',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('text', models.CharField(max_length=3000)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('user', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to=posts.models.get_image_path, blank=True)),
                ('hodnotenie', models.CharField(max_length=50)),
            ],
        ),
    ]
