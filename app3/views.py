from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1> Soy el Index de la App3 <h1>")

def pagina3(request):
    html="""
     <p> Soy el parrafo de la App3. <p>
     <h2> Soy un Subtitulo de la App3<h2>
     """
    return HttpResponse(html)