from rest_framework import viewsets
from liberator import serializers


class ArticleViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ArticleSerializer

    queryset = serializer_class.Meta.model.objects.all()
