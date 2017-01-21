from rest_framework import serializers

from liberator import models


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """
    class Meta:
        model = models.User
        depth = 1
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'groups',
            'user_permissions',
            'password'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = models.User(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            is_active=validated_data["is_active"],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
