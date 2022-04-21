
from pydoc import doc
from django.http import HttpResponse
from django.shortcuts import render
from AppOne.models import Integrantes

# Create your views here.

def integrantes(self):
    integrantes = Integrantes(nombre='Carmelo' , edad= 46 , fechaDnacimiento='26/05/1981')
    integrantes.save()
    docDtext = f'NOMBRE:{integrantes.nombre}  EDAD:{integrantes.edad}  Fecha De Nacimiento:{integrantes.fechaDnacimiento}'
    return HttpResponse(docDtext)
def integrantes1(self):
    integrantes1 = Integrantes(nombre='Romina' , edad= 26 , fechaDnacimiento = '22/03/1995')
    integrantes1.save()
    docDtext = f'NOMBRE:{integrantes1.nombre}  EDAD:{integrantes1.edad}  Fecha De Nacimiento:{integrantes1.fechaDnacimiento}'
    return HttpResponse(docDtext)
def integrantes2(self):
    integrantes2 = Integrantes(nombre='Juan' , edad=20, fechaDnacimiento = '13/01/2003') 
    integrantes2.save()
    docDtext = f'NOMBRE:{integrantes2.nombre}  EDAD:{integrantes2.edad}  Fecha De Nacimiento:{integrantes2.fechaDnacimiento}'
    return HttpResponse(docDtext)
