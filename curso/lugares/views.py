from django.shortcuts import render
from functions import *
from principal import *

# Create your views here.
def mostrarLugares(request):
 lugar = "Zacatecas"
 comentarios=[]
 actividades=[]

 xmlTree=getTreeContent()
 comentarios=getTextTree(xmlTree)
 comentarios=depureComments(comentarios,lugar)
 actividades=serchActivities(comentarios)

 context = {
     'lugar': lugar,
     'comentarios':comentarios,
     'actividades':actividades,
    }
    # devolvemos los datos a la vista saludo.html para printarlos
 return render(request, 'lugares.html', context)
