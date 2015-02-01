from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from . import views


router_v1 = DefaultRouter()
router_v1.register(r'articles', views.ArticleViewSet)
router_v1.register(r'article-states', views.ArticleStateViewSet)
router_v1.register(r'article-titles', views.ArticleTitleViewSet)
router_v1.register(r'article-content', views.ArticleContentViewSet)
router_v1.register(r'issues', views.IssueViewSet)
router_v1.register(r'issue-titles', views.IssueTitleViewSet)
router_v1.register(r'languages', views.LanguageViewSet)
router_v1.register(r'sections', views.SectionViewSet)
router_v1.register(r'section-titles', views.SectionTitleViewSet)
router_v1.register(r'series', views.SerieViewSet)
router_v1.register(r'serie-titles', views.SerieTitleViewSet)
router_v1.register(r'users', views.UserViewSet)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^v1/',
        include(
            router_v1.urls,
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
