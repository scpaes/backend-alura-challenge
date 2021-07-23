from django.db import models


class Video(models.Model):
    titulo = models.CharField(verbose_name='Título',max_length=30)
    descricao = models.TextField(verbose_name='Descrição',max_length=100)
    url = models.URLField(verbose_name='url')

    def __str__(self) -> str:
        return self.titulo