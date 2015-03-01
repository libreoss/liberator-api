from rest_framework import serializers

from liberator import models


class IssueTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IssueTitle
        fields = (
            'title',
            'language',
        )


class IssueSerializer(serializers.ModelSerializer):
    titles = IssueTitleSerializer(many=True)

    class Meta:
        model = models.Issue
        fields = (
            'id',
            'publication_date',
            'titles',
        )

    def create(self, data):
        publication_date = data['publication_date']

        issue = models.Issue.objects.create(publication_date=publication_date)
        issue.save()

        for title_instance in data['titles']:
            title_data = {
                'title': title_instance['title'],
                'issue_id': issue.pk,
                'language_id': title_instance['language'].pk,
            }
            title = models.IssueTitle.objects.create(**title_data)
            title.save()

        return issue
