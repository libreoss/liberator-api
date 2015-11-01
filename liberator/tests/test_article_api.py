#from rest_framework.test import APITestCase
#from liberator.factories import ArticleFactory, AdminFactory
## from rest_framework.response import Response
#from django.http.response import HttpResponseNotFound
#
#
#class TestArticle(APITestCase):
#    def setUp(self):
#        super(TestArticle, self).setUp()
#        self.admin = AdminFactory()
#        self.client.force_authenticate(user=self.admin)
#
#        # self.state = ArticleFactory()
#        # self.state.save()
#        # self.language = liberator.factories.LanguageFactory()
#        # self.language.save()
#
#    def test_create_article_simple(self):
#        self.fail("Finish this test")
#
#    def test_create_article_without_content(self):
#        self.fail("Finish this test")
#
#    def test_create_article_without_authors(self):
#        self.fail("Finish this test")
#
#    def test_create_article_without_authors_and_content(self):
#        self.fail("Finish this test")
#
#    def test_read_article_list(self):
#        article = ArticleFactory()
#        article.save()
#
#        url = '/api/v1/articles/'
#        response = self.client.get(url)
#
#        self.assertNotIsInstance(response, HttpResponseNotFound)
#        self.assertGreater(len(response.data), 0)
#
#        print(response.data)
#
#
##         article_title = liberator.factories.ArticleTitleFactory(
##             article=article,
##             language=self.language
##         )
##         article_title.save()
##         article_content = liberator.factories.ArticleContentFactory(
##             article=article,
##             language=self.language
##         )
##         article_content.save()
##         url = '/api/v1/articles/{0}/'.format(article.id)
##         article_api = self.client.get(url, **self.args)
##         self.assertEqual(article.pk, article_api.data['id'])
##         self.assertEqual(article.state.id, article_api.data['state'])
##         title = article.titles.get(pk=article_title.pk)
##         title_api = article_api.data['titles'][0]
##         self.assertEqual(title.title, title_api['title'])
##         self.assertEqual(title.language.pk, title_api['language'])
##         content = article.contents.get(pk=article_content.pk)
##         content_api = article_api.data['contents'][0]
##         self.assertEqual(content.content, content_api['content'])
##         self.assertEqual(content.language.pk, content_api['language'])
##
##
## class TestStateArticle(TestCase):
##     def test_create_article_state(self):
##         article_state = liberator.factories.ArticleStateFactory()
##         article_state.save()
##         url = '/api/v1/article-states/{0}/'.format(article_state.id)
##         article_state_api = self.client.get(url, **self.args)
##         self.assertEqual(article_state.pk, article_state_api.data['id'])
##         self.assertEqual(article_state.name, article_state_api.data['name'])
