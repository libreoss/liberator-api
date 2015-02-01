from rest_framework import serializers

from liberator import models


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Section


class SectionTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SectionTitle
