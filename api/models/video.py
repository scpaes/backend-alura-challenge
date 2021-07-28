from django.db import models
from api.models.categorias import Categorias


class Video(models.Model):
    titulo = models.CharField(verbose_name='Título',max_length=30)
    descricao = models.TextField(verbose_name='Descrição',max_length=100)
    url = models.URLField(verbose_name='url')
    categoriaID = models.ForeignKey(Categorias, blank=False, null=False, default=1, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo