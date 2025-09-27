from rest_framework import serializers
from .models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()  # muestra el nombre de la categoría

    class Meta:
        model = Producto
        fields = "__all__"
