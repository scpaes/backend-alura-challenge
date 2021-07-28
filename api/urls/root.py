from django.urls import path
from django.urls.conf import include
from rest_framework import routers

from api.views.video import VideoViewset, VideoCategoriaViewset
from api.views.categoria import CategoriaViewset

router = routers.DefaultRouter()
router.register('videos', VideoViewset, basename='videos')
router.register('categorias', CategoriaViewset, basename='categorias')


urlpatterns = [
    path('', include(router.urls), name='api'),
    path('categorias/<int:pk>/videos/', VideoCategoriaViewset.as_view({'get': 'list'}), name='video-categoria')
]