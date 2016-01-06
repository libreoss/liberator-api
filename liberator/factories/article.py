import factory

import liberator.models


class ArticleFactory(factory.Factory):
    class Meta:
        model = liberator.models.Article

    @factory.post_generation
    def issues(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        if extracted:
            # A list of issues were passed in, use them
            for issue in extracted:
                self.issues.add(issue)
