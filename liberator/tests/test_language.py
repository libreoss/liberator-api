from . import TestCase
# from liberator.factories import LanguageFactory


# class TestLanguage(TestCase):
#     def test_create_language(self):
#         language = LanguageFactory()
#         language.save()
#         url = '/api/v1/languages/{0}/'.format(language.pk)
#         language_api = self.client.get(url, **self.args)
#         self.assertEqual(language.pk, language_api.data['id'])
#         self.assertEqual(language.name, language_api.data['name'])
