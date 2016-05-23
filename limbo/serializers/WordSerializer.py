

from rest_framework import serializers


class WordSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=60)
