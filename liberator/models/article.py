from django.db import models
from django.conf import settings

from .issue import Issue
from .section import Section


class Article(models.Model):

    authors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="articles"
    )

    section = models.ForeignKey(Section, related_name="articles", null=True, blank=True)

    issues = models.ManyToManyField(Issue, related_name="articles")
