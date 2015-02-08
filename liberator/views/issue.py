from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from liberator import serializers


class IssueViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.IssueSerializer
    queryset = serializer_class.Meta.model.objects.all()


class IssueTitleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.IssueTitleSerializer
    queryset = serializer_class.Meta.model.objects.all()
