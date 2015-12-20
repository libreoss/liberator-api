
from rest_framework import viewsets
from liberator import serializers


class MediaViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.MediaSerializer

    queryset = serializer_class.Meta.model.objects.all()
