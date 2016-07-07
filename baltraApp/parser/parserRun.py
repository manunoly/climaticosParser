__author__ = 'manuel'

from estacionQuito import estacionQuito
from baltraParser import baltra
from mongomodels import *
import datetime
import os

try:
    connect("clima")
    estacionQuitoObj = estacionQuito()
    objetos = estacionQuitoObj.parser()
    if (objetos.__len__() > 0):
        Clima.objects.insert(objetos)
        for fichero_actual in estacionQuitoObj.ficheros:
            os.rename(estacionQuitoObj.getCaminoOrigen()+fichero_actual,estacionQuitoObj.getCaminoDestino() + fichero_actual)
    if(estacionQuitoObj.ficherosR.__len__()>0):
        for fichero_actual in estacionQuitoObj.ficherosR:
            os.rename(estacionQuitoObj.getCaminoOrigen()+fichero_actual,estacionQuitoObj.getCaminoDuplicados() + fichero_actual)
except Exception, e:
    fichero_actual = estacionQuitoObj.ficheros[estacionQuitoObj.ficheros.__len__()-1]
    ficheroLog = open(estacionQuitoObj.getLog(), 'a')
    ficheroLog.write(str(datetime.datetime.now()) + " " + str(fichero_actual) + " " + e.message)
    ficheroLog.write("\n")
    ficheroLog.close()
    os.rename(estacionQuitoObj.getCaminoOrigen()+fichero_actual,estacionQuitoObj.getError() + fichero_actual)

try:
    baltraP = baltra()
    objetos = baltraP.parserBaltra()
    if (objetos.__len__() > 0):
        Clima.objects.insert(objetos)
        for fichero_actual in baltraP.ficheros:
            os.rename(baltraP.getCaminoOrigen()+fichero_actual,baltraP.getCaminoDestino() + fichero_actual)
    if(baltraP.ficherosR.__len__()>0):
        for fichero_actual in baltraP.ficherosR:
            os.rename(baltraP.getCaminoOrigen()+fichero_actual,baltraP.getCaminoDuplicados() + fichero_actual)

except Exception, e:
    fichero_actual = baltraP.ficheros[baltraP.ficheros.__len__()-1]
    ficheroLog = open(baltraP.getLog(), 'a')
    ficheroLog.write(str(datetime.datetime.now()) + " " + str(fichero_actual) + " " + e.message)
    ficheroLog.write("\n")
    ficheroLog.close()
    os.rename(baltraP.getCaminoOrigen()+fichero_actual,baltraP.getError() + fichero_actual)