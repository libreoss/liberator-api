from django.db import models

from .language import Language


class Serie(models.Model):
    """
    Seerie
    """
    def __str__(self):
        titles = SerieTitle.objects.filter(serie=self)
        if len(titles) == 0:
            return "???"
        return " . ".join([title.__str__() for title in titles])


class SerieTitle(models.Model):
    """
    Title of the serie
    """

    serie = models.ForeignKey(Serie, related_name='titles')
    """
    Serie the title belongs to
    """

    language = models.ForeignKey(Language)
    """
    Language the title is written in
    """

    title = models.CharField(max_length=60)
    """
    The title
    """

    def __str__(self):
        return "{title} ({language})".format(
            language=self.language.name,
            title=self.title
        )
