from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from . import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'articles', views.ArticleViewSet)
router.register(r'languages', views.LanguageViewSet)
router.register(r'states', views.StateViewSet)
router.register(r'issues', views.IssueViewSet)
router.register(r'sections', views.SectionViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'contents', views.ContentViewSet)
router.register(r'media', views.MediaViewSet)

sections_router = routers.NestedSimpleRouter(
    router,
    r'sections',
    lookup='section'
)
sections_router.register(
    r'articles',
    views.SectionArticleViewSet,
    base_name='section-article'
)

issues_router = routers.NestedSimpleRouter(
    router, r'issues',
    lookup='issues'
)
issues_router.register(
    r'articles',
    views.IssueArticleViewSet,
    base_name='issue-article'
)

articles_router = routers.NestedSimpleRouter(
    router,
    r'articles',
    lookup='article'
)
articles_router.register(
    r'languages',
    views.ArticleLanguageViewSet,
    base_name='article-language'
)

urlpatterns = patterns(
    '',
    url(
        r'',
        include(
            router.urls,
        ),
    ),

    # Nested section endpoints
    url(
        r'',
        include(
            sections_router.urls,
        ),
    ),
    url(
        r'',
        include(
            issues_router.urls,
        ),
    ),
    url(
        r'',
        include(
            articles_router.urls,
        ),
    ),
    
    url(r'^upload/(?P<articleId>\d+)/$', views.UploadMediaView.as_view()),

    url(
        r'^auth/',
        'rest_framework_jwt.views.obtain_jwt_token',
        name='login',
    ),
    url(
        r'^token-refresh/',
        'rest_framework_jwt.views.refresh_jwt_token'
    ),
)
