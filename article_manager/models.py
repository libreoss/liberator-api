from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    source = models.CharField(unique=True, max_length=48)
    contents_cyr = models.TextField()
    contents_lat = models.TextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
