from rest_framework import serializers

from liberator import models


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Serie


class SerieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SerieTitle
