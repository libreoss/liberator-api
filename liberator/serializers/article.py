from rest_framework import serializers

from liberator import models


class ArticleTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleTitle
        fields = (
            'title',
            'language',
            'revision',
            'revision_author',
        )


class ArticleContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleContent
        fields = (
            'content',
            'language',
            'revision',
            'revision_author',
        )


class ArticleSerializer(serializers.ModelSerializer):
    titles = ArticleTitleSerializer(many=True)
    contents = ArticleContentSerializer(many=True)

    class Meta:
        model = models.Article
        fields = (
            'id',
            'authors',
            'state',
            'section',
            'serie',
            'serie_part',
            'issue',
            'titles',
            'contents',
        )

    def create(self, data):
        state = data['state']
        article = models.Article.objects.create(
            state=state,
        )
        article.save()

        for author in data['authors']:
            article.authors.add(author)

        for title_instance in data['titles']:
            title_data = {
                'title': title_instance['title'],
                'article_id': article.pk,
                'language_id': title_instance['language'].pk,
                'revision_author_id': title_instance.get(
                    'revision_author_id',
                    self.context['request'].user
                ).pk,
            }
            title = models.ArticleTitle.objects.create(**title_data)
            title.save()

        for content_instance in data['contents']:
            content_data = {
                'article_id': article.pk,
                'language_id': content_instance['language'].pk,
                'content': content_instance.get('content', ''),
                'revision_author_id': content_instance.get(
                    'revision_author_id',
                    self.context['request'].user
                ).pk,
            }
            content = models.ArticleContent.objects.create(**content_data)
            content.save()

        return article


class ArticleStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleState
