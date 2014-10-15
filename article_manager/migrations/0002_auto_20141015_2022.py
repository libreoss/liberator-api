# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='source',
            field=models.URLField(unique=True),
        ),
    ]
