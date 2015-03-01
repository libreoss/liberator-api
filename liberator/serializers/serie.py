from rest_framework import serializers

from liberator import models


class SerieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SerieTitle
        fields = (
            'title',
            'language',
        )


class SerieSerializer(serializers.ModelSerializer):
    titles = SerieTitleSerializer(many=True)

    class Meta:
        model = models.Serie
        fields = (
            'id',
            'titles',
        )

    def create(self, data):
        serie = models.Serie.objects.create()
        serie.save()

        for title_instance in data['titles']:
            title_data = {
                'title': title_instance['title'],
                'serie_id': serie.pk,
                'language_id': title_instance['language'].pk,
            }
            title = models.SerieTitle.objects.create(**title_data)
            title.save()

        return serie
