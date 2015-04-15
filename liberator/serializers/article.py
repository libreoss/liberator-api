from rest_framework import serializers

from liberator import models


class ArticleTitleSerializer(serializers.ModelSerializer):
    """
    ArticleTitleSerializer
    """
    class Meta:
        model = models.ArticleTitle
        fields = (
            'title',
            'language',
            'revision',
            'revision_author',
        )


class ArticleContentSerializer(serializers.ModelSerializer):
    """
    ArticleContentSerializer
    """
    class Meta:
        model = models.ArticleContent
        fields = (
            'content',
            'language',
            'revision',
            'revision_author',
        )


class ArticleStateSerializer(serializers.ModelSerializer):
    """
    Article state serializer
    """
    class Meta:
        model = models.ArticleState


class ArticleSerializer(serializers.ModelSerializer):
    """
    ArticleSerializer
    """

    titles = ArticleTitleSerializer(many=True)
    """
    Titles of the article in different languages
    """

    contents = ArticleContentSerializer(many=True, required=False)
    """
    Contents of the article in different languages
    """

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
        """
        Create the article, title and content in one request
        """

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

        for content_instance in data.get('contents', []):
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
