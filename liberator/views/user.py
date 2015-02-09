from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework_extensions.mixins import NestedViewSetMixin

from liberator import serializers


class UserViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def pre_save(self, obj):
        """
        Handle user password
        """
        if 'password' in self.request._data:
            obj.set_password(obj.password)

    @list_route(methods=['get'])
    def me(self, request):
        serializer = serializers.UserSerializer(request.user)
        return Response(serializer.data)
