import factory

import liberator.models
from .language import LanguageFactory


class SerieFactory(factory.Factory):
    class Meta:
        pass
        # model = liberator.models.Serie


class SerieTitleFactory(factory.Factory):
    class Meta:
        pass
        # model = liberator.models.SerieTitle

    # serie = factory.SubFactory(SerieFactory)
    # language = factory.SubFactory(LanguageFactory)
    title = 'Title'
