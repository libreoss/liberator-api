from django.db import models

from .language import Language

class Issue(models.Model):
    publication_date = models.DateTimeField()

class IssueTitle(models.Model):
    issue = models.ForeignKey(Issue)
    language = models.ForeignKey(Language)
    title = models.CharField(max_length=60)

