from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from liberator import serializers, models


class SerieViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Serie endpoint view
    """

    serializer_class = serializers.SerieSerializer
    """
    Serializer class
    """

    queryset = serializer_class.Meta.model.objects.all()
    """
    Queryset
    """


class SerieTitleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Serie title endpoint view
    """

    serializer_class = serializers.SerieTitleSerializer
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
        serie_id = parents_query_dict['serie']
        serie = models.Serie.objects.get(pk=serie_id)
        serializer.save(serie=serie)
