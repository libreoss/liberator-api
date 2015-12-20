
from rest_framework import viewsets
from liberator import serializers


class IssueViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.IssueSerializer

    queryset = serializer_class.Meta.model.objects.all()
