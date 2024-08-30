from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1> Soy el Index de la App1 <h1>")

def presentacion(request):
    html="""
     <p> Soy el parrafo de la App1. <p>
     <h2> Soy un Subtitulo de la App1<h2>
     """
    return HttpResponse(html)
