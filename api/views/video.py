from api.helpers.videoserializer import VideoSerializer
from api.models.video import Video
from rest_framework import views, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class VideoViewset(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['titulo']


class VideoCategoriaViewset(viewsets.ModelViewSet):
    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.filter(categoriaID=self.kwargs['pk'])
