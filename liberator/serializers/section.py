from rest_framework import serializers

from liberator import models


class SectionTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SectionTitle
        fields = (
            'title',
            'language',
        )


class SectionSerializer(serializers.ModelSerializer):
    titles = SectionTitleSerializer(many=True)

    class Meta:
        model = models.Section
        fields = (
            'id',
            'titles'
        )

    def create(self, data):
        section = models.Section.objects.create()
        section.save()

        for title_instance in data['titles']:
            title_data = {
                'title': title_instance['title'],
                'section_id': section.pk,
                'language_id': title_instance['language'].pk,
            }
            title = models.SectionTitle.objects.create(**title_data)
            title.save()

        return section
