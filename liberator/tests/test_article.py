import liberator.models
from . import TestCase


class TestArticle(TestCase):
    def setUp(self):
        super(TestArticle, self).setUp()
        self.state = liberator.models.ArticleState.objects.create(
            name='published'
        )

    def test_create_article(self):
        article = liberator.models.Article.objects.create(
            state=self.state
        )
        url = '/api/v1/articles/{0}/'.format(article.id)
        article_api = self.client.get(url, **self.args)
        self.assertEqual(article.pk, article_api.data['id'])
        self.assertEqual(article.state.id, article_api.data['state'])
