from django.urls import path
from django.urls.conf import include
from rest_framework import routers

from api.views.video import VideoViewset

router = routers.DefaultRouter()
router.register('videos', VideoViewset, basename='videos')

urlpatterns = [
    path('', include(router.urls), name='api')
]