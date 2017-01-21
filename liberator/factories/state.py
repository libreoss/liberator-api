import factory

import liberator.models


class StateFactory(factory.Factory):
    class Meta:
        model = liberator.models.State
    name = "state1"
    order = 1
