from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'articles', views.ArticleViewSet)
# router.register(r'languages', views.LanguageViewSet)
# router.register(r'article-states', views.ArticleStateViewSet)
# router.register(r'issues', views.IssueViewSet)
# router.register(r'sections', views.SectionViewSet)
# router.register(r'series', views.SerieViewSet)
# router.register(r'titles', views.ArticleTitleViewSet)
#
urlpatterns = patterns(
    '',
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
