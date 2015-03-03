from django.db import models

from .language import Language


class Issue(models.Model):
    publication_date = models.DateTimeField()

    def __str__(self):
        titles = IssueTitle.objects.filter(issue=self)
        if len(titles) == 0:
            return "???"
        return " • ".join([title.__str__() for title in titles])


class IssueTitle(models.Model):
    issue = models.ForeignKey(Issue, related_name='titles')
    language = models.ForeignKey(Language)
    title = models.CharField(max_length=60)

    def __str__(self):
        return "{title} ({language})".format(
            language=self.language.name,
            title=self.title
        )
