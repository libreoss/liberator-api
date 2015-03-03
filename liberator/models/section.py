from django.db import models

from .language import Language


class Section(models.Model):
    def __str__(self):
        titles = SectionTitle.objects.filter(section=self)
        if len(titles) == 0:
            return "???"
        return " • ".join([title.__str__() for title in titles])


class SectionTitle(models.Model):
    section = models.ForeignKey(Section, related_name='titles')
    language = models.ForeignKey(Language)
    title = models.CharField(max_length=60)

    def __str__(self):
        return "{title} ({language})".format(
            language=self.language.name,
            title=self.title
        )
