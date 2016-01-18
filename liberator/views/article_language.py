

from rest_framework import viewsets
from liberator import serializers

from rest_framework.response import Response
from rest_framework.decorators import list_route

from liberator.models import Language


class ArticleLanguageViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.ContentSerializer

    queryset = serializer_class.Meta.model.objects.all()

    def list(self, request, pk=None, language_pk=None):
        contents = self.queryset.filter(
            article=pk
        ).filter(
            language=language_pk
        ).order_by("date")
        serializer = self.serializer_class(contents, many=True)
        return Response(serializer.data)

    @list_route()
    def latest(self, request, article_pk=None):
        languages = Language.objects.all()
        contents = [] 
        for lang in languages:
            content = self.queryset.filter(
                article=article_pk,
                language=lang.pk
            ).order_by("date").last()
            contents.append(content)
        serializer = self.serializer_class(contents, many=True)
        return Response(serializer.data)
