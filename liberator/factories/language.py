

import factory

import liberator.models

class LanguageFactory(factory.Factory):
    class Meta:
        model = liberator.models.Language
    name = "language1" 
