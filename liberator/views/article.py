from rest_framework import viewsets

from liberator import serializers


class ArticleStateViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArticleStateSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ArticleTitleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArticleTitleSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ArticleContentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArticleContentSerializer
    queryset = serializer_class.Meta.model.objects.all()
