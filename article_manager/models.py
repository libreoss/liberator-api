from django.db import models

from article_manager.libre import LibreManager 

from django.conf import settings 

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    source_lat = models.CharField(unique=True, max_length=48)
    source_cyr = models.CharField(unique=True, max_length=48)
    contents_cyr = models.TextField()
    contents_lat = models.TextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def fromDokuwikiArticle(article): 
        title = article.getTitle()
        slug = article.getId() 
        author = article.getAuthor()
        lat = parsed_article.getLatHTML()
        cyr = ""
        if article.isCyr():
            cyr = article.getHTML()
        entry = Article()
        entry.name = title 
        entry.author = author
        if article.isCyr():
            entry.source_cyr = slug
            entry.source_lat = ""
        else: 
            entry.source_lat = slug 
            entry.source_cyr = ""
        entry.contents_lat = lat
        entry.contents_cyr = cyr
        return entry

    def fromRemote(slug): 
        remote = LibreManager(settings.DOKUWIKI_USERNAME, settings.DOKUWIKI_PASSWORD)
        return self.fromDokuwikiArticle(remote.getPage(slug))
