
from rest_framework import viewsets
from liberator import serializers


class IssueViewSet(NestedViewSetMixin, viewsets.ModelViewSet):

    serializer_class = serializers.IssueSerializer

    queryset = serializer_class.Meta.model.objects.all()
