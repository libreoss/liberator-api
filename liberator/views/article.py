from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin
from re import match

from liberator import serializers, models


class ArticleStateViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Article state endpoint view
    """

    serializer_class = serializers.ArticleStateSerializer
    """
    Serializer class
    """

    queryset = serializer_class.Meta.model.objects.all()
    """
    Queryset
    """


class ArticleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Article endpoint view
    """

    serializer_class = serializers.ArticleSerializer
    """
    Serializer class
    """

    queryset = serializer_class.Meta.model.objects.all()
    """
    Queryset
    """


class ArticleTitleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Article title endpoint view
    """

    serializer_class = serializers.ArticleTitleSerializer
    """
    Serializer class
    """

    queryset = serializer_class.Meta.model.objects.all()
    """
    Queryset
    """

    def perform_create(self, serializer):
        parents_query_dict = self.get_parents_query_dict()
        article_id = parents_query_dict['article']
        article = models.Article.objects.get(pk=article_id)
        serializer.save(article=article)


class ArticleContentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Article content endpoint view
    """

    serializer_class = serializers.ArticleContentSerializer
    """
    Serializer class
    """

    queryset = serializer_class.Meta.model.objects.all()
    """
    Queryset
    """

    def perform_create(self, serializer):
        """
        Perform create
        """
        parents_query_dict = self.get_parents_query_dict()
        article_id = parents_query_dict['article']
        article = models.Article.objects.get(pk=article_id)
        serializer.save(article=article)
