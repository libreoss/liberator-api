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

sections_router = routers.NestedSimpleRouter(router, r'sections', lookup='section')
sections_router.register(r'articles', views.SectionArticleViewSet, base_name='section-article')

urlpatterns = patterns(
    '',
    url(
        r'^v1/',
        include(
            router.urls,
        ),
    ),

    # Nested section endpoints
    url(
        r'^v1/',
        include(
            sections_router.urls,
        ),
    ),

    url(
        r'^v1/auth/',
        'rest_framework_jwt.views.obtain_jwt_token',
        name='login',
    ),
    url(
        r'^v1/token-refresh/',
        'rest_framework_jwt.views.refresh_jwt_token'
    ),
    # url(
    #     r'^$',
    #     include(
    #         'rest_framework.urls',
    #         namespace='rest_framework',
    #     ),
    # ),
)
