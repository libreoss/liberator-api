from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from liberator import serializers


class LanguageViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Language endpoint view
    """

    serializer_class = serializers.LanguageSerializer
    """
    Serializer class
    """

    queryset = serializer_class.Meta.model.objects.all()
    """
    Queryset
    """
