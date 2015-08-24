
from django.db import models

from .article import Article


class Media(models.Model):

    article = models.ForeignKey(Article, related_name="media")

    url = models.CharField(max_length=1024)
