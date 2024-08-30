from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pagina1 (request):
    html="""
     <h1 style="color:pink"> Titulo App 2 </h1>
     """
    return  HttpResponse(html)
    
