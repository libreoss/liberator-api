from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from liberator import serializers, models


class IssueViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.IssueSerializer
    """
    Serializer class
    """

    queryset = serializer_class.Meta.model.objects.all()
    """
    Queryset
    """


class IssueTitleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.IssueTitleSerializer
    """
    Serializer class
    """

    queryset = serializer_class.Meta.model.objects.all()
    """
    Queryset
    """

    def perform_create(self, serializer):
        """
        Perform create
        """
        parents_query_dict = self.get_parents_query_dict()
        issue_id = parents_query_dict['issue']
        issue = models.Issue.objects.get(pk=issue_id)
        serializer.save(issue=issue)
