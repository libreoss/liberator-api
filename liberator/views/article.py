from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from liberator import serializers


class ArticleStateViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.ArticleStateSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ArticleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ArticleTitleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.ArticleTitleSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ArticleContentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.ArticleContentSerializer
    queryset = serializer_class.Meta.model.objects.all()
