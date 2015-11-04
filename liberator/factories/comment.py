
import factory

import liberator.models

from .article import ArticleFactory 
from .user import UserFactory 

class CommentFactory(factory.Factory):
    class Meta:
        model = liberator.models.Comment
    
    article = factory.SubFactory(ArticleFactory)
    author =factory.SubFactory(UserFactory)
