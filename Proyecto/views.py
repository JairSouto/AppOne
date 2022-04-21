
from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context


def TemplateModel(self):
    nombre1 = 'Carmelo'
    edad1 = 46
    FechaDnacimiento1 = '26/05/1981'
    nombre2 ='Romina'
    edad2= 26
    FechaDnacimiento2 = '22/03/1995'
    nombre3= 'Juan'
    edad3= 20
    FechaDnacimiento3='13/01/2003'
   
    diccionario = {'Carmelo':nombre1,  'C_edad':edad1, 'FdNacimineto_C':FechaDnacimiento1, 'Romina':nombre2, 'R_edad':edad2 , 'R_FdN':FechaDnacimiento2, 'Juan':nombre3, 'J_edad':edad3 , 'FdN_J':FechaDnacimiento3}
    miHTml = open('C:/Users/ASUS-PC/Desktop/Projecto01/Proyecto/plantillas/temple.html')
    plantilla = Template(miHTml.read())
    miHTml.close()
    cnTxTo= Context(diccionario)
    documento = plantilla.render(cnTxTo)
    return HttpResponse(documento)