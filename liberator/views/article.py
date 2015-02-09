from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin
from re import match

from liberator import serializers, models


class ArticleStateViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.ArticleStateSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ArticleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ArticleTitleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.ArticleTitleSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def perform_create(self, serializer):
        parents_query_dict = self.get_parents_query_dict()
        article_id = parents_query_dict['article']
        article = models.Article.objects.get(pk=article_id)
        serializer.save(article=article)


class ArticleContentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.ArticleContentSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def perform_create(self, serializer):
        parents_query_dict = self.get_parents_query_dict()
        article_id = parents_query_dict['article']
        article = models.Article.objects.get(pk=article_id)
        serializer.save(article=article)
