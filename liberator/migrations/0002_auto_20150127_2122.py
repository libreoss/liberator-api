# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liberator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='serie',
            field=models.ForeignKey(to='liberator.Serie', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='serie_part',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
