from rest_framework import serializers

from liberator import models

class IssueSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Issue
        fields = (
            "id",
            "name",
            "special", 
            "publication_date"
        )
