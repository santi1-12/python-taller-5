from django.urls import path
from . import views

urlpatterns = [
    # Categorías
    path("categorias/crear/", views.crear_categoria, name="crear_categoria"),
    path("categorias/<int:pk>/actualizar/", views.actualizar_categoria, name="actualizar_categoria"),
    path("categorias/<int:pk>/eliminar/", views.eliminar_categoria, name="eliminar_categoria"),

    # Productos
    path("productos/crear/", views.crear_producto, name="crear_producto"),
    path("productos/<int:pk>/actualizar/", views.actualizar_producto, name="actualizar_producto"),
    path("productos/<int:pk>/eliminar/", views.eliminar_producto, name="eliminar_producto"),
]
