from django.db import models
from django.conf import settings

from .issue import Issue
from .language import Language
from .section import Section
from .serie import Serie


class ArticleState(models.Model):
    """
    State of an article
    """

    name = models.CharField(max_length=30)
    """ Name of the state """

    sort_order = models.IntegerField(blank=True, null=True)
    """ Sorting order """

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    Article class which points to list of authors, titles and contents
    """

    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, help_text='Authors of this article')
    """
    Authors of the article
    """

    state = models.ForeignKey(ArticleState)
    """
    State of the article
    """

    section = models.ForeignKey(Section, blank=True, null=True)
    """
    Section of the article
    """

    serie = models.ForeignKey(Serie, blank=True, null=True)
    """
    Serie of the article
    """

    serie_part = models.IntegerField(blank=True, null=True)
    """
    Part in a serie of articles
    """

    issue = models.ForeignKey(Issue, blank=True, null=True)
    """
    Issue
    """

    def __str__(self):
        titles = ArticleTitle.objects.filter(article=self)
        if len(titles) == 0:
            return "???"
        return " . ".join(
            [
                title.__str__()
                for title in titles
            ]
        )


class ArticleTitle(models.Model):
    """
    Article Title I have no idea why is it here
    """

    article = models.ForeignKey(Article, related_name='titles')
    """
    Article this title belongs to
    """

    language = models.ForeignKey(Language)
    """
    Language in which the title was written in
    """

    title = models.CharField(max_length=180)
    """
    The title
    """

    revision = models.IntegerField(blank=True, null=True)
    """
    Revision of the title
    """

    revision_timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    """
    Time when of the last revision
    """

    revision_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True
    )
    """
    Author of the revision
    """

    def __str__(self):
        return "{title} ({language})".format(
            language=self.language.name,
            title=self.title
        )


class ArticleContent(models.Model):
    """
    Content of the article
    """

    article = models.ForeignKey(Article, related_name='contents')
    """
    Article the content belongs to
    """

    language = models.ForeignKey(Language)
    """
    Language in which the content was written in
    """

    content = models.TextField()
    """
    The content
    """

    revision = models.IntegerField(blank=True, null=True)
    """
    Revision of the content
    """

    revision_timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    """
    Time when of the last revision
    """

    revision_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True
    )
    """
    Author of the revision
    """


    def __str__(self):
        title = ArticleTitle.objects.filter(
            article=self.article,
            language=self.language
        ).first()
        if title is None:
            return "???"
        return title.title
