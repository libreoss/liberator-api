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


class ArticleContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleContent
