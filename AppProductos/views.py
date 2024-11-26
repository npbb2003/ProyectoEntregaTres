from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def inicio(req):

    return render(req, "appproductos/index.html")


def sesionesFotograficas(req):

    return render(req, "appproductos/sesionesFotograficas.html")


def copiasImpresas(req):

    return render(req, "appproductos/copias.html")


def fotolibros(req):

    return render(req, "appproductos/fotolibros.html")
