from rest_framework import serializers

from liberator import models


class ArticleStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleState


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article


class ArticleTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleTitle
        fields = (
            'title',
            'language',
            'revision',
            'revision_author',
        )



class ArticleContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleContent
        fields = (
            'content',
            'language',
            'revision',
            'revision_author',
        )
