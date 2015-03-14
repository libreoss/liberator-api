from django.db import models

from .language import Language


class Issue(models.Model):
    """
    Issue
    """

    publication_date = models.DateTimeField()
    """
    Time of publication
    """

    def __str__(self):
        titles = IssueTitle.objects.filter(issue=self)
        if len(titles) == 0:
            return "???"
        return " . ".join([title.__str__() for title in titles])


class IssueTitle(models.Model):
    """
    Title of the issue
    """

    issue = models.ForeignKey(Issue, related_name='titles')
    """
    Issue this title belongs to
    """

    language = models.ForeignKey(Language)
    """
    Language which the title was written in
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
