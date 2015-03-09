import liberator.models
from . import TestCase
from liberator.factories import ArticleFactory, ArticleStateFactory


class TestArticle(TestCase):
    def setUp(self):
        super(TestArticle, self).setUp()
        self.state = ArticleStateFactory()
        self.state.save()

    def test_create_article(self):
        article = ArticleFactory(state=self.state)
        article.save()
        url = '/api/v1/articles/{0}/'.format(article.id)
        article_api = self.client.get(url, **self.args)
        self.assertEqual(article.pk, article_api.data['id'])
        self.assertEqual(article.state.id, article_api.data['state'])
