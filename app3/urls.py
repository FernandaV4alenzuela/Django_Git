from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls), #Eliminar esta mmda una vez llegados aqui
    path('', views.index),
    path('pagina3/', views.pagina3),
]