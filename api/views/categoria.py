from api.models.video import Video
from rest_framework import viewsets
from api.models.categorias import Categorias
from api.helpers.categoriaserializer import CategoriaSerialier


class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriaSerialier

    def get_queryset(self):
       return Categorias.objects.all()
