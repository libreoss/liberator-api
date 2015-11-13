from rest_framework import serializers

from liberator import models

class IssueSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Issue
        fields = (
            "name",
            "special", 
            "published", 
            "publishing_date"
        )
