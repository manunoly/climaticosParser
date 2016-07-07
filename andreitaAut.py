__author__ = 'manuel'
import os

'''
Validar que esten 4 ficheros por cada clima.

1 leer nombres de ficheros de 1 dir
1.1 picar por el punto para evitar extension
2 tomar primer nombre
3 buscar en cliclo cuantos nombres hay similares
4 si estan las cantidades adecuada borrar
5 si no estan las cantidades adecuadas
6 imprimir ficheros errados y borrar
'''

caminoFicheros = "/home/manuel/andreitaTest/datos_climaticos_designbuilder"
ficheros = os.listdir(caminoFicheros)

def solostring(s):
    if isinstance(s, str):
        return True
    elif isinstance(s, unicode):
        return False
    else:
        return False

listaFicheros = []
ficherosRevisar = []
if ficheros.__len__() > 1:
    for fichero in ficheros:
        root, ext = os.path.splitext(fichero)
        name = os.path.basename(root)
        listaFicheros.append(name)
    for fichero in listaFicheros:
        repeticiones = listaFicheros.count(fichero)
        if repeticiones != 4:
            if fichero not in ficherosRevisar:
                ficherosRevisar.append(fichero)
    for fichero in ficheros:
            root, ext = os.path.splitext(fichero)
            name = os.path.basename(root)
            if name in ficherosRevisar:
                os.remove(caminoFicheros+"/"+fichero)
                print "eliminando el fichero " + fichero
#print("revisar estos ficheros \n" + ficherosRevisar.__str__())

