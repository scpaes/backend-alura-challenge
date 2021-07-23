from api.helpers.videoserializer import VideoSerializer
from api.models.video import Video
from rest_framework import viewsets

class VideoViewset(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    