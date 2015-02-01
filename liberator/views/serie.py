from rest_framework import viewsets

from liberator import serializers


class SerieViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SerieSerializer
    queryset = serializer_class.Meta.model.objects.all()


class SerieTitleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SerieTitleSerializer
    queryset = serializer_class.Meta.model.objects.all()
