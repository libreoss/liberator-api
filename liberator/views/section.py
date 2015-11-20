
from rest_framework import viewsets
from liberator import serializers


class SectionViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.SectionSerializer

    queryset = serializer_class.Meta.model.objects.all()
