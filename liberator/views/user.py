from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework_extensions.mixins import NestedViewSetMixin

from liberator import serializers


class UserViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    User endpoint view
    """

    serializer_class = serializers.UserSerializer
    """
    Serializer class
    """

    queryset = serializer_class.Meta.model.objects.all()
    """
    Queryset
    """

    def pre_save(self, obj):
        """
        Handle user password
        """
        if 'password' in self.request._data:
            obj.set_password(obj.password)

    @list_route(methods=['get'])
    def me(self, request):
        """
        Return info about logged in user
        """
        serializer = serializers.UserSerializer(request.user)
        return Response(serializer.data)
