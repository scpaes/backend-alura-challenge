from rest_framework.generics import ListAPIView
from api.models.video import Video
from api.helpers.videoserializer import VideoSerializer
from rest_framework.decorators import authentication_classes, permission_classes

@authentication_classes([])
@permission_classes([])
class VideoFreeListView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = []
    authentication_classes = []

    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        print('here.')
        return super().get(request, *args, **kwargs)

    
    def list(self, request, *args, **kwargs):
        print('here.')
        return super().list(request, *args, **kwargs)

