from rest_framework import serializers

from liberator import models


class MediaSerializer(serializers.ModelSerializer):

    article = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.Media
        fields = (
            "id",
            "article",
            "url"
        )
