from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def inicio(req):

    return render(req, "appproductos/index.html")


def sesionesFotograficas(req):

    return HttpResponse("vista sesiones fotograficas")


def copiasImpresas(req):

    return HttpResponse("vista copias impresas")


def fotolibros(req):

    return HttpResponse("vista fotolibros")
