from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from liberator import serializers, models


class SerieViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.SerieSerializer
    queryset = serializer_class.Meta.model.objects.all()


class SerieTitleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.SerieTitleSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def perform_create(self, serializer):
        parents_query_dict = self.get_parents_query_dict()
        serie_id = parents_query_dict['serie']
        serie = models.Serie.objects.get(pk=serie_id)
        serializer.save(serie=serie)
