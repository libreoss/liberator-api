
import factory
import datetime
from factory import LazyAttribute
import liberator.models

from .article import ArticleFactory
from .user import UserFactory
from .language import LanguageFactory
from .state import StateFactory


class IssueFactory(factory.Factory):
    class Meta:
        model = liberator.models.Issue
    name = "issue1"
    publication_date = LazyAttribute(lambda o: datetime.datetime.utcnow())
