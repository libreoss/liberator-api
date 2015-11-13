
from rest_framework import viewsets
from liberator import serializers


class StateViewSet(NestedViewSetMixin, viewsets.ModelViewSet):

    serializer_class = serializers.StateSerializer

    queryset = serializer_class.Meta.model.objects.all()
