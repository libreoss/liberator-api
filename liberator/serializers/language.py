from rest_framework import serializers

from liberator import models


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
