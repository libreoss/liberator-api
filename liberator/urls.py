from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from . import views


router_v1 = DefaultRouter()
router_v1.register(r'users', views.UserViewSet)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^api/v1/',
        include(
            router_v1.urls,
        ),
    ),
    url(
        r'^api/v1/auth/',
        'rest_framework_jwt.views.obtain_jwt_token',
        name='login',
    ),
    url(
        r'^api/$',
        include(
            'rest_framework.urls',
            namespace='rest_framework',
        ),
    ),
)
