from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_framework_extensions.routers import ExtendedDefaultRouter

from . import views


router = ExtendedDefaultRouter()
router.register(r'languages', views.LanguageViewSet)
router.register(r'article-states', views.ArticleStateViewSet)
router.register(r'users', views.UserViewSet)

article = router.register(r'articles', views.ArticleViewSet)
article.register(
    r'titles',
    views.ArticleTitleViewSet,
    base_name='articles-title',
    parents_query_lookups=['article']
)
article.register(
    r'contents',
    views.ArticleContentViewSet,
    base_name='articles-content',
    parents_query_lookups=['article']
)

router.register(r'issues', views.IssueViewSet).register(
    r'titles',
    views.IssueTitleViewSet,
    base_name='issues-title',
    parents_query_lookups=['issue']
)

router.register(r'sections', views.SectionViewSet).register(
    r'titles',
    views.SectionTitleViewSet,
    base_name='sections-title',
    parents_query_lookups=['section']
)

router.register(r'series', views.SerieViewSet).register(
    r'titles',
    views.SerieTitleViewSet,
    base_name='series-title',
    parents_query_lookups=['serie']
)


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^v1/',
        include(
            router.urls,
        ),
    ),
    url(
        r'^v1/auth/',
        'rest_framework_jwt.views.obtain_jwt_token',
        name='login',
    ),
    url(
        r'^$',
        include(
            'rest_framework.urls',
            namespace='rest_framework',
        ),
    ),
)
