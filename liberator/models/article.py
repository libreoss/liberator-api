from django.db import models
from django.conf import settings
from .section import Section
from .serie import Serie
from .issue import Issue
from .language import Language
from .user import User


class ArticleState(models.Model):
    name = models.CharField(max_length=30)
    sort_order = models.IntegerField(blank=True, null=True)


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    state = models.ForeignKey(ArticleState)
    section = models.ForeignKey(Section, blank=True, null=True)
    serie = models.ForeignKey(Serie, blank=True, null=True)
    serie_part = models.IntegerField(blank=True, null=True)
    issue = models.ForeignKey(Issue, blank=True, null=True)


class ArticleTitle(models.Model):
    article = models.ForeignKey(Article)
    language = models.ForeignKey(Language)
    title = models.CharField(max_length=180)
    revision = models.IntegerField(blank=True)
    revision_timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    revision_author = models.ForeignKey(settings.AUTH_USER_MODEL)


class ArticleContent(models.Model):
    article = models.ForeignKey(Article)
    language = models.ForeignKey(Language)
    content = models.TextField()
    revision = models.IntegerField(blank=True)
    revision_timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    revision_author = models.ForeignKey(settings.AUTH_USER_MODEL)
