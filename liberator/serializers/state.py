from rest_framework import serializers

from liberator import models

class StateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.State
        fields = (
            "id",
            "name",
            "order"
        )
