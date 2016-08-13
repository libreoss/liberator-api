from rest_framework import serializers

from liberator import models

from .user import *

from liberator.models import Article


class CommentSerializer(serializers.ModelSerializer):

    article = serializers.PrimaryKeyRelatedField(
        queryset=Article.objects.all()
    )
    author = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=UserSerializer.Meta.model.objects.all()
    )

    class Meta:

        model = models.Comment
        fields = (
            "id",
            "article",
            "author",
            "date",
            "text"
        )
