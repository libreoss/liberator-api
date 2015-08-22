
from django.db import models
from django.conf import settings

from .article import Article
from .language import Language
from .state import State

import django.utils.timezone as timezone


class Content(models.Model):

    article = models.ForeignKey(Article, related_name="contents")

    language = models.ForeignKey(Language)

    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    date = models.DateField(default=timezone.now())

    title = models.CharField(max_length=64)

    text = models.CharField(max_length=16384)

    state = models.ForeignKey(State)
