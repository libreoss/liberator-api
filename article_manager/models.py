from django.db import models

from article_manager.libre import LibreManager 

from django.contrib.auth.models import User as Author

from django.conf import settings 

# Create your models here.
class Category(models.Model): 
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def __unicode__(self): 
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=64)
    source_lat = models.CharField(max_length=48)
    source_cyr = models.CharField(max_length=48)
    contents_cyr = models.TextField()
    contents_lat = models.TextField()
    author = models.ForeignKey(Author)
    stage = models.IntegerField(default = 0)
    issue = models.IntegerField(blank = True, null = True)
    category = models.ForeignKey(Category, blank = True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def fromDokuwikiArticle(article): 
        title = article.getTitle()
        slug = article.getId() 
        try:
            author = Author.objects.get(username = article.getAuthor())
        except Author.DoesNotExist:
            author = Author.objects.get(username = "nobody")
        lat = article.getLatHTML()
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
        entry = Article.fromDokuwikiArticle(remote.getPage(slug))
        entry.wiki_slug = slug
        return entry

    def titleInDatabase(self): 
        """
        Returns Article object with same title if it exists

        None otherwise

        NOTE: This can be also used to check wether title exists in database
        """
        try:
            if Article.objects.filter(name = self.name).exists():
                return Article.objects.get(name = self.name)
            else: 
                return None 
        except Exception:
            return None # TODO Better handle this case

    def slugInDatabase(slug): 
        """
        Returns True if slug is in database 

        False otherwise  
        """
        return Article.objects.filter(source_lat = slug).exists() or Article.objects.filter(source_cyr = slug).exists()

    def approve(self, cat, issue): 
        """
        This is method used when approving articles, each article has to contain its assigned issue and category, these are 
        provided by arguments cat and issue. 

        cat - Category object representing particular category 
        issue: integer representing issue number 

        This method modifies object. 

        """
        self.issue = issue
        self.category = cat
