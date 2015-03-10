import liberator.models
import factory


class LanguageFactory(factory.Factory):
    class Meta:
        model = liberator.models.Language

    name = 'English'
