from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'liberator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^manager/', 'article_manager.views.articles_list'),
    url(r"manager/articles/(?P<article_id>\d+)", "article_manager.views.article_view"),
    url(r'^admin/', include(admin.site.urls)),
)
