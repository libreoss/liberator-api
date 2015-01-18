from django.contrib import admin

from article_manager.models import Article, Category


admin.site.register(Article)
admin.site.register(Category)
