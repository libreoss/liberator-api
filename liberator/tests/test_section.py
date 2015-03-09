import liberator.models
from . import TestCase
import liberator.factories


class TestSection(TestCase):
    def setUp(self):
        super(TestSection, self).setUp()
        self.language = liberator.factories.LanguageFactory()
        self.language.save()

    def test_create_section(self):
        section = liberator.factories.SectionFactory()
        section.save()
        section_title = liberator.factories.SectionTitleFactory(
            section=section,
            language=self.language
        )
        section_title.save()
        url = '/api/v1/sections/{0}/'.format(section.pk)
        section_api = self.client.get(url, **self.args)
        self.assertEqual(section.pk, section_api.data['id'])
        title = section.titles.get(pk=section_title.pk)
        title_api = section_api.data['titles'][0]
        self.assertEqual(title.title, title_api['title'])
        self.assertEqual(title.language.pk, title_api['language'])
