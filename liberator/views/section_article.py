

from rest_framework import viewsets
from liberator import serializers

from rest_framework.response import Response


class SectionArticleViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ArticleSerializer

    queryset = serializer_class.Meta.model.objects.all()

    def list(self, request, pk=None, section_pk=None):
        articles = self.queryset.filter(section=section_pk)
        serializer = self.serializer_class(articles, many=True)
        return Response(serializer.data)
