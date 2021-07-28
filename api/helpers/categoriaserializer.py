from django.db.models import fields
from api.models.categorias import Categorias
from rest_framework import serializers


class CategoriaSerialier(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'