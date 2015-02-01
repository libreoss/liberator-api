from rest_framework import viewsets

from liberator import serializers


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IssueSerializer
    queryset = serializer_class.Meta.model.objects.all()


class IssueTitleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IssueTitleSerializer
    queryset = serializer_class.Meta.model.objects.all()
