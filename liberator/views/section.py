from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from liberator import serializers, models


class SectionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.SectionSerializer
    queryset = serializer_class.Meta.model.objects.all()


class SectionTitleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.SectionTitleSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def perform_create(self, serializer):
        parents_query_dict = self.get_parents_query_dict()
        section_id = parents_query_dict['section']
        section = models.Section.objects.get(pk=section_id)
        serializer.save(section=section)
