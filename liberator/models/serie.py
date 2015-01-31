from django.db import models

from .language import Language


class Serie(models.Model):
    pass


class SerieTitle(models.Model):
    serie = models.ForeignKey(Serie)
    language = models.ForeignKey(Language)
    title = models.CharField(max_length=60)
