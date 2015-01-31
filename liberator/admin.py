from django.contrib import admin

from .models import \
    Article, \
    ArticleContent, \
    ArticleState, \
    ArticleTitle, \
    Issue, \
    IssueTitle, \
    Language, \
    Section, \
    SectionTitle, \
    Serie, \
    SerieTitle

admin.site.register(Article)
admin.site.register(ArticleContent)
admin.site.register(ArticleState)
admin.site.register(ArticleTitle)
admin.site.register(Issue)
admin.site.register(IssueTitle)
admin.site.register(Language)
admin.site.register(Section)
admin.site.register(SectionTitle)
admin.site.register(Serie)
admin.site.register(SerieTitle)
