
import factory

import liberator.models

from .article import ArticleFactory 

class MediaFactory(factory.Factory):
    class Meta:
        model = liberator.models.Media
    
    article = factory.SubFactory(ArticleFactory)
    url = "https://somemedia.com/media.jpg"

