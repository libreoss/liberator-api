import factory

import liberator.models


class SectionFactory(factory.Factory):
    class Meta:
        model = liberator.models.Section
    name = "section1"

