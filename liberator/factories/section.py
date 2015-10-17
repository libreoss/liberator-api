import factory

import liberator.models
from .language import LanguageFactory


class SectionFactory(factory.Factory):
    class Meta:
        pass
        # model = liberator.models.Section


class SectionTitleFactory(factory.Factory):
    class Meta:
        pass
        # model = liberator.models.SectionTitle

    # section = factory.SubFactory(SectionFactory)
    # language = factory.SubFactory(LanguageFactory)
    title = 'Title'
