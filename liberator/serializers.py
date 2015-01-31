from rest_framework import serializers

from . import models


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


class ArticleStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleState
