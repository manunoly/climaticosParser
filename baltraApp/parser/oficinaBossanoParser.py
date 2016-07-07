__author__ = 'manuel'

from mongomodels import *
import datetime
import os
from parser import parserGeneral

class oficinaBossano(parserGeneral):
    ficheros = []
    carpetas = []
    def parserOficinaBossano(self):
        fileList = []
        for root, subFolders, files in os.walk(self.getCaminoOrigen()):
            carpeta = root.replace(self.getCaminoOrigen(),"")
            if(carpeta != ""):
                self.carpetas.append(carpeta)
            for file in files:
                fileList.append(os.path.join(root, file))
        objetos = []
        for file in fileList:
            if (file.endswith('.TXT')):
                self.ficheros.append(file)
                data = open(file,'r')
                linias = data.readlines()
                fecha = linias[0].rsplit()[25][:10]
                fecha = datetime.datetime(int(fecha[:2]) + 2000,int(fecha[2:4]),int(fecha[4:6]),int(fecha[6:8]),int(fecha[8:10]),00)
                data.close()
                datos = ""
                if (Clima.objects(Q(fichero=file) & Q(fecha=fecha)).count() == 0):
                    for dato in linias:
                        datos = dato.rsplit()
                        climaObj = Clima()
                        climaObj.__setitem__("Estacion","OficinaBossano")
                        climaObj.__setitem__("fecha", datetime.datetime(int(datos[25][:2]) + 2000,int(datos[25][2:4]),int(datos[25][4:6]),int(datos[25][6:8]),int(datos[25][8:10]),00))
                        climaObj.__setitem__("segundos",float(datos[0]))
                        climaObj.__setitem__("temperaturaSensor0",float(datos[1]))
                        climaObj.__setitem__("temperaturaSensor1",float(datos[2]))
                        climaObj.__setitem__("temperaturaSensor2",float(datos[3]))
                        climaObj.__setitem__("temperaturaSensor3",float(datos[4]))
                        climaObj.__setitem__("temperaturaSensor4",float(datos[5]))
                        climaObj.__setitem__("temperaturaSensor5",float(datos[6]))
                        climaObj.__setitem__("temperaturaSensor6",float(datos[7]))
                        climaObj.__setitem__("temperaturaSensor7",float(datos[8]))
                        climaObj.__setitem__("temperaturaSensor8",float(datos[9]))
                        climaObj.__setitem__("temperaturaSensor9",float(datos[10]))
                        climaObj.__setitem__("temperaturaSensor10",float(datos[11]))
                        climaObj.__setitem__("temperaturaSensor11",float(datos[12]))
                        climaObj.__setitem__("temperaturaSensor12",float(datos[13]))
                        climaObj.__setitem__("temperaturaSensor13",float(datos[14]))
                        climaObj.__setitem__("temperaturaSensor14",float(datos[15]))
                        climaObj.__setitem__("temperaturaSensor15",float(datos[16]))
                        climaObj.__setitem__("iluminacionSensor1",float(datos[17]))
                        climaObj.__setitem__("iluminacionSensor2",float(datos[18]))
                        climaObj.__setitem__("iluminacionSensor3",float(datos[19]))
                        climaObj.__setitem__("dioxidoCarbono",float(datos[20]))
                        climaObj.__setitem__("humedadRelativa",float(datos[21]))
                        if (float(datos[22])<0):
                            climaObj.__setitem__("personas",0)
                        else:
                            climaObj.__setitem__("personas",int(float(datos[22])))
                        climaObj.__setitem__("potenciaLuminica",float(datos[23]))
                        climaObj.__setitem__("potenciaEquipos",float(datos[24]))
                        climaObj.__setitem__("fichero",file)
                        objetos.append(climaObj)
        del datos,linias
        return objetos