import liberator.models
from . import TestCase
import liberator.factories


# class TestSerie(TestCase):
#     def setUp(self):
#         super(TestSerie, self).setUp()
#         self.language = liberator.factories.LanguageFactory()
#         self.language.save()
#
#     def test_create_serie(self):
#         serie = liberator.factories.SerieFactory()
#         serie.save()
#         serie_title = liberator.factories.SerieTitleFactory(
#             serie=serie,
#             language=self.language
#         )
#         serie_title.save()
#         url = '/api/v1/series/{0}/'.format(serie.pk)
#         serie_api = self.client.get(url, **self.args)
#         self.assertEqual(serie.pk, serie_api.data['id'])
#         title = serie.titles.get(pk=serie_title.pk)
#         title_api = serie_api.data['titles'][0]
#         self.assertEqual(title.title, title_api['title'])
#         self.assertEqual(title.language.pk, title_api['language'])
