from django.urls import path
from AppProductos import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("fotolibros/", views.fotolibros, name="fotolibros"),
    path("copiasImpresas/", views.copiasImpresas, name="copias"),
    path(
        "sesionesFotograficas/", views.sesionesFotograficas, name="sesionesFotograficas"
    ),
]
