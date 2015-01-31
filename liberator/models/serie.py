from django.db import models

from .language import Language


class Serie(models.Model):
    def __str__(self):
        titles = SerieTitle.objects.filter(serie=self)
        if len(titles) == 0:
            return "???"
        return " • ".join([title.__str__() for title in titles])

class SerieTitle(models.Model):
    serie = models.ForeignKey(Serie)
    language = models.ForeignKey(Language)
    title = models.CharField(max_length=60)

    def __str__(self):
        return "{title} ({language})".format(language=self.language.name, title=self.title)
