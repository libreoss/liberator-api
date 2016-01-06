from rest_framework import serializers

from liberator import models

from .issue import *
from .section import *
from .user import *
from .comment import *
from .media import *

from rest_framework.serializers import PrimaryKeyRelatedField


class ArticleSerializer(serializers.ModelSerializer):

    queryset = UserSerializer.Meta.model.objects.all()
    authors = PrimaryKeyRelatedField(
        many=True,
        queryset=queryset
    )
    section = PrimaryKeyRelatedField(
        queryset=SectionSerializer.Meta.model.objects.all(),
        required=False
    )
    issues = PrimaryKeyRelatedField(
        many=True,
        queryset=models.Issue.objects.all()
    )
    contents = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='content-detail'
    )
    comments = CommentSerializer(many=True, read_only=True)
    media = MediaSerializer(many=True, read_only=True)

    class Meta:
        model = models.Article
        fields = (
            "id",
            "authors",
            "section",
            "issues",
            "comments",
            "contents",
            "media",
        )
