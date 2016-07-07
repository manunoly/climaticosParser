__author__ = 'manuel'

from baltraParser import *
# from baltraApp.mongomodels import *
from mongomodels import *

connect("clima")

# for dato in clima.objects.fields(slice__temperaturaAireMinima__eq = 1):
# for dato in clima.objects(Temperatura__gt = {"Temperatura": { "temperaturaAireMinima": 0.2}}):
#     print dato.Temperatura


baltraP = baltra()
objetos = baltraP.parserBaltra()
if (objetos.__len__() > 0):
    Clima.objects.insert(objetos)


# clima = clima()
# connect("clima")
# clima.prueba = "asdfsdf"
# clima.numero = 12
# clima.datos = "datos { asd : 1211}"
# clima.save()
