from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from liberator import serializers


class SerieViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.SerieSerializer
    queryset = serializer_class.Meta.model.objects.all()


class SerieTitleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.SerieTitleSerializer
    queryset = serializer_class.Meta.model.objects.all()
