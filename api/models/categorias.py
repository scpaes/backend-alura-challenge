from django.db import models


class Categorias(models.Model):
    titulo = models.CharField(max_length=30)
    cor = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.titulo
