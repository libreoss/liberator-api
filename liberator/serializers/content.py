from rest_framework import serializers

from liberator import models

from .user import *
from .language import *
from .article import *
from .state import *


class ContentSerializer(serializers.ModelSerializer):

    article = serializers.PrimaryKeyRelatedField(
        queryset=ArticleSerializer.Meta.model.objects.all()
    )
    language = serializers.PrimaryKeyRelatedField(
        queryset=LanguageSerializer.Meta.model.objects.all()
    )
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    state = serializers.PrimaryKeyRelatedField(
        queryset=StateSerializer.Meta.model.objects.all()
    )

    class Meta:

        model = models.Content
        fields = (
            "id",
            "article",
            "language",
            "author",
            "date",
            "title",
            "text",
            "state"
        )
