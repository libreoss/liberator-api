import liberator.models
from . import TestCase
import liberator.factories


class TestArticle(TestCase):
    def setUp(self):
        super(TestArticle, self).setUp()
        self.state = liberator.factories.ArticleStateFactory()
        self.state.save()
        self.language = liberator.factories.LanguageFactory()
        self.language.save()

    def test_create_article(self):
        article = liberator.factories.ArticleFactory(state=self.state)
        article.save()
        article_title = liberator.factories.ArticleTitleFactory(
            article=article,
            language=self.language
        )
        article_title.save()
        article_content = liberator.factories.ArticleContentFactory(
            article=article,
            language=self.language
        )
        article_content.save()
        url = '/api/v1/articles/{0}/'.format(article.id)
        article_api = self.client.get(url, **self.args)
        self.assertEqual(article.pk, article_api.data['id'])
        self.assertEqual(article.state.id, article_api.data['state'])
        title = article.titles.get(pk=article_title.pk)
        title_api = article_api.data['titles'][0]
        self.assertEqual(title.title, title_api['title'])
        self.assertEqual(title.language.pk, title_api['language'])
        content = article.contents.get(pk=article_content.pk)
        content_api = article_api.data['contents'][0]
        self.assertEqual(content.content, content_api['content'])
        self.assertEqual(content.language.pk, content_api['language'])


class TestStateArticle(TestCase):
    def test_create_article_state(self):
        article_state = liberator.factories.ArticleStateFactory()
        article_state.save()
        url = '/api/v1/article-states/{0}/'.format(article_state.id)
        article_state_api = self.client.get(url, **self.args)
        self.assertEqual(article_state.pk, article_state_api.data['id'])
        self.assertEqual(article_state.name, article_state_api.data['name'])
