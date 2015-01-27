# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleContent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('content', models.TextField()),
                ('revision', models.IntegerField(blank=True)),
                ('revision_timestamp', models.DateTimeField(auto_now_add=True, auto_now=True)),
                ('article', models.ForeignKey(to='liberator.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleState',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleTitle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=180)),
                ('revision', models.IntegerField(blank=True)),
                ('revision_timestamp', models.DateTimeField(auto_now_add=True, auto_now=True)),
                ('article', models.ForeignKey(to='liberator.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('publication_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IssueTitle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=60)),
                ('issue', models.ForeignKey(to='liberator.Issue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SectionTitle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=60)),
                ('language', models.ForeignKey(to='liberator.Language')),
                ('section', models.ForeignKey(to='liberator.Section')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SerieTitle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=60)),
                ('language', models.ForeignKey(to='liberator.Language')),
                ('serie', models.ForeignKey(to='liberator.Serie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='issuetitle',
            name='language',
            field=models.ForeignKey(to='liberator.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articletitle',
            name='language',
            field=models.ForeignKey(to='liberator.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articletitle',
            name='revision_author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articlecontent',
            name='language',
            field=models.ForeignKey(to='liberator.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articlecontent',
            name='revision_author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='issue',
            field=models.ForeignKey(null=True, to='liberator.Issue', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.ForeignKey(null=True, to='liberator.Section', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='state',
            field=models.ForeignKey(to='liberator.ArticleState'),
            preserve_default=True,
        ),
    ]
