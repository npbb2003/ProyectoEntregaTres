from django.urls import path
from AppProductos import views

urlpatterns = [
    path("inicio/", views.inicio),
    path("fotolibros/", views.fotolibros),
    path("copiasImpresas/", views.copiasImpresas),
    path("sesIonesFotograficas/", views.sesionesFotograficas),
]
