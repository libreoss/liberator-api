from rest_framework import serializers

from liberator import models


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Issue


class IssueTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IssueTitle
        fields = (
            'title',
            'language',
        )
