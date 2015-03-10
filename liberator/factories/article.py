import factory

import liberator.models
from .language import LanguageFactory


class ArticleFactory(factory.Factory):
    class Meta:
        model = liberator.models.Article


class ArticleStateFactory(factory.Factory):
    class Meta:
        model = liberator.models.ArticleState

    name = 'published'


class ArticleTitleFactory(factory.Factory):
    class Meta:
        model = liberator.models.ArticleTitle

    article = factory.SubFactory(ArticleFactory)
    language = factory.SubFactory(LanguageFactory)
    title = 'Title'


class ArticleContentFactory(factory.Factory):
    class Meta:
        model = liberator.models.ArticleContent

    article = factory.SubFactory(ArticleFactory)
    language = factory.SubFactory(LanguageFactory)
    content = 'Content'
