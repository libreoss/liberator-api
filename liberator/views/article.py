
from rest_framework import viewsets
from liberator import serializers
from liberator.models import Article, Media
from liberator.serializers import MediaSerializer
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

class ArticleViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ArticleSerializer

    queryset = serializer_class.Meta.model.objects.all()

    @detail_route()
    def media(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        result = Media.objects.filter(article=article)
        serializer = MediaSerializer(result, many=True)
        return Response(serializer.data)
