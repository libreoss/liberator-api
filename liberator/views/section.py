from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from liberator import serializers


class SectionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.SectionSerializer
    queryset = serializer_class.Meta.model.objects.all()


class SectionTitleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.SectionTitleSerializer
    queryset = serializer_class.Meta.model.objects.all()
