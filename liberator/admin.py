from django.contrib.auth import get_user_model
from django.contrib import admin

from .models import (
    Article,
    Comment,
    Content,
    Media,
    Issue,
    Language,
    Section,
    State,
)


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Content)
admin.site.register(Media)
admin.site.register(Issue)
admin.site.register(Language)
admin.site.register(Section)
admin.site.register(State)
admin.site.register(get_user_model())
