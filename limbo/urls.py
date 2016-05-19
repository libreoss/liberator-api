from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from . import views

router = routers.SimpleRouter()
router.register(r'limbo', views.LimboViewSet, base_name="limbo")


urlpatterns = patterns(
    '',
    url(
        r'',
        include(
            router.urls,
        ),
    ),

)
