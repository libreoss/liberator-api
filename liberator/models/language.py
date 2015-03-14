from django.db import models


class Language(models.Model):
    """
    Language
    """

    name = models.CharField(max_length=30)
    """
    The name of the language
    """

    def __str__(self):
        return self.name
