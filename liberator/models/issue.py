from django.db import models


class Issue(models.Model):

    name = models.CharField(max_length=64)

    special = models.BooleanField(default=False)

    publication_date = models.DateTimeField(blank=True, null=True)
