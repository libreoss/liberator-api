from django.db import models

from .language import Language


class Section(models.Model):
    pass


class SectionTitle(models.Model):
    section = models.ForeignKey(Section)
    language = models.ForeignKey(Language)
    title = models.CharField(max_length=60)
