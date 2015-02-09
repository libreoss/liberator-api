from rest_framework import serializers

from liberator import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        write_only_fields = ('password',)
        depth = 1
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'groups',
            'user_permissions',
        )
