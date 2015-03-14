from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from liberator import serializers, models


class SectionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Section endpoint view
    """

    serializer_class = serializers.SectionSerializer
    """
    Serializer class
    """

    queryset = serializer_class.Meta.model.objects.all()
    """
    Queryset
    """


class SectionTitleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Section title endpoint view
    """

    serializer_class = serializers.SectionTitleSerializer
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
        section_id = parents_query_dict['section']
        section = models.Section.objects.get(pk=section_id)
        serializer.save(section=section)
