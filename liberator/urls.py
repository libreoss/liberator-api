from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'liberator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^manager/', 'article_manager.views.article_manager_base_view'),
    url(r'^admin/', include(admin.site.urls)),
)
