from rest_framework import serializers

from liberator import models

from .user import * 

class ContentSerializer(serializers.ModelSerializer):
    
    article = serializers.PrimaryKeyRelatedField(read_only=True)
    language = serializers.PrimaryKeyRelatedField(read_only=True)
    author = UserSerializer()
    state = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.Content
        fields = (
            "article",
            "language",
            "author", 
            "date", 
            "title", 
            "text",
            "state"
        )
