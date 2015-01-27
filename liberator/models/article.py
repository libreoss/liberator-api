from django.db import models

from .section import Section
from .issue import Issue
from .language import Language
from django.contrib.auth.models import User as Author

class ArticleState(models.Model):
    name = models.CharField(max_length=30)
    sort_order = models.IntegerField(blank=True, null=True)

class Article(models.Model):
    author = models.ForeignKey(Author)
    state = models.ForeignKey(ArticleState)
    section = models.ForeignKey(Section, blank=True, null=True)
    issue = models.ForeignKey(Issue, blank=True, null=True)

class ArticleTitle(models.Model):
    article = models.ForeignKey(Article)
    language = models.ForeignKey(Language)
    title = models.CharField(max_length=180)
    revision = models.IntegerField(blank=True)
    revision_timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    revision_author = models.ForeignKey(Author)

class ArticleContent(models.Model):
    article = models.ForeignKey(Article)
    language = models.ForeignKey(Language)
    content = models.TextField()
    revision = models.IntegerField(blank=True)
    revision_timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    revision_author = models.ForeignKey(Author)
