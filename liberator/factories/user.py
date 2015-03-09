import liberator.models
import factory


class UserFactory(factory.Factory):
    class Meta:
        model = liberator.models.User

    first_name = 'John'
    last_name = 'Doe'
    is_staff = False
    is_active = True
    email = factory.LazyAttribute(
        lambda a: '{0}.{1}@example.com'.format(
            a.first_name,
            a.last_name
        ).lower())
