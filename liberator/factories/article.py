import liberator.models
import factory


class ArticleFactory(factory.Factory):
    class Meta:
        model = liberator.models.Article


class ArticleStateFactory(factory.Factory):
    class Meta:
        model = liberator.models.ArticleState

    name = 'published'
