import factory

import liberator.models
from .language import LanguageFactory
from datetime import datetime


class IssueFactory(factory.Factory):
    class Meta:
        pass
        # model = liberator.models.Issue

    publication_date = datetime.now()


class IssueTitleFactory(factory.Factory):
    class Meta:
        pass
        # model = liberator.models.IssueTitle

    # issue = factory.SubFactory(IssueFactory)
    # language = factory.SubFactory(LanguageFactory)
    title = 'Title'
