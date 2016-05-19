
from .WordSerializer import WordSerializer
from rest_framework import serializers

class LimboSerializer(serializers.Serializer):
    words = WordSerializer(many=True)
