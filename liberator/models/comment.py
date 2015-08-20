
from django.db import models
from django.conf import settings

import django.utils.timezone as timezone

from .article import Article

class Comment(models.Model):
    
    article = models.ForeignKey(Article, related_name="comments")

    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    date = models.DateField(default=timezone.now())
    
    text = models.CharField(max_length=4096)
