from rest_framework import serializers

from liberator import models

from .user import * 

class CommentSerializer(serializers.ModelSerializer):
    
    article = serializers.PrimaryKeyRelatedField(read_only=True)
    author = UserSerializer()
    class Meta:
        model = models.Comment
        fields = (
            "id",
            "article",
            "author", 
            "date", 
            "text"
        )
