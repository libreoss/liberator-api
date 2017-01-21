
import factory

import liberator.models

from .article import ArticleFactory
from .user import UserFactory
from .language import LanguageFactory
from .state import StateFactory


class ContentFactory(factory.Factory):
    class Meta:
        model = liberator.models.Content

    article = factory.SubFactory(ArticleFactory)
    author = factory.SubFactory(UserFactory)
    language = factory.SubFactory(LanguageFactory)
    title = "Some title"
    text = "Some text"
    state = factory.SubFactory(StateFactory)
