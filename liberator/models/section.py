from django.db import models

from .language import Language


class Section(models.Model):
    """
    Section
    """
    def __str__(self):
        titles = SectionTitle.objects.filter(section=self)
        if len(titles) == 0:
            return "???"
        return " . ".join([title.__str__() for title in titles])


class SectionTitle(models.Model):
    """
    Title of the section
    """

    section = models.ForeignKey(Section, related_name='titles')
    """
    Section the title belongs to
    """

    language = models.ForeignKey(Language)
    """
    Language the title was written in
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
