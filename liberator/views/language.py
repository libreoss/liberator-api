
from rest_framework import viewsets
from liberator import serializers


class LanguageViewSet(NestedViewSetMixin, viewsets.ModelViewSet):

    serializer_class = serializers.LanguageSerializer

    queryset = serializer_class.Meta.model.objects.all()
