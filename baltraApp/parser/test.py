__author__ = 'manuel'

from baltraParser import baltra
from mongomodels import *
import datetime
import os, errno

connect("clima")
obj = Clima()
oficinaBossano = baltra()
objetos = oficinaBossano.parserBaltra()
exit()

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

try:
    connect("clima")
    obj = Clima()
    a = obj._object_key.iteritems()
    # exit()
    oficinaBossano = baltra()
    objetos = oficinaBossano.parserBaltra()
    print objetos.__len__()
    if (objetos.__len__() > 0):             
        Clima.objects.insert(objetos)

    for fichero_actual in oficinaBossano.ficheros:
        try:
            os.rename(fichero_actual, fichero_actual.replace(oficinaBossano.getCaminoOrigen(),oficinaBossano.getCaminoDestino()))
        except Exception:
            mkdir_p(fichero_actual.replace(oficinaBossano.getCaminoOrigen(),oficinaBossano.getCaminoDestino()).rsplit('/',1)[0])
            os.rename(fichero_actual, fichero_actual.replace(oficinaBossano.getCaminoOrigen(),oficinaBossano.getCaminoDestino()))
except Exception, e:
    ficheroLog = open(oficinaBossano.getLog(), 'a')
    ficheroLog.write(str(datetime.datetime.now()) + " " + str(oficinaBossano.ficheros) + " " + e.message)
    ficheroLog.write("\n")
    ficheroLog.close()
    if (oficinaBossano.ficheros.__len__()>= 1):
        fichero_actual = oficinaBossano.ficheros[oficinaBossano.ficheros.__len__()-1]
        try:
            os.rename(fichero_actual,fichero_actual.replace(oficinaBossano.getCaminoOrigen(),oficinaBossano.getError()))
        except Exception:
            mkdir_p(fichero_actual.replace(oficinaBossano.getCaminoOrigen(),oficinaBossano.getError()).rsplit('/',1)[0])
            os.rename(fichero_actual,fichero_actual.replace(oficinaBossano.getCaminoOrigen(),oficinaBossano.getError()))

