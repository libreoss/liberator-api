# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=64)),
                ('source', models.URLField()),
                ('contents_cyr', models.TextField()),
                ('contents_lat', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
