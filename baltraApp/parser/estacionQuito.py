__author__ = 'manuel'
from parser import parserGeneral
import os
from mongomodels import *
import datetime

class estacionQuito(parserGeneral):
    ficheros = []
    ficherosR = []
    def parser(self):
        path = self.getCaminoOrigen()
        dirs = os.listdir(path)
        objetos = []

        for file in dirs:
            if (file.endswith('.txt')):
                current_file = os.path.join(path, file)
                existeF = Clima.objects(fichero=file)
                if(not existeF):
                    self.ficheros.append(file)
                    data = open(current_file,'r')
                    contenido = data.readlines()
                    data.close()
                    for line in contenido:
                        if("/" in line):
                            datosArr = line.replace("---","-9999").rsplit()
                            fecha = datosArr[0].split("/")
                            anno = int(fecha[2]) + 2000
                            mes = int(fecha[1])
                            dia = int(fecha[0])
                            hora = datosArr[1].split(":")
                            minuto = int(hora[1])
                            hora = int(hora[0])

                            climaObj = Clima()
                            climaObj.__setitem__("Estacion","EstacionQuito")
                            climaObj.__setitem__("fecha", datetime.datetime(anno,mes,dia,hora,minuto,00))
                            climaObj.__setitem__("temperaturaExterior",float(datosArr[2]))
                            climaObj.__setitem__("temperaturaExteriorMaxima",float(datosArr[3]))
                            climaObj.__setitem__("temperaturaExteriorMinima",float(datosArr[4]))
                            climaObj.__setitem__("temperaturaAparente",float(datosArr[12]))
                            climaObj.__setitem__("temperaturaAparenteIndiceCalentamiento",float(datosArr[13]))
                            climaObj.__setitem__("temperaturaAparenteTHW",float(datosArr[14]))
                            climaObj.__setitem__("temperaturaAparenteTHSW",float(datosArr[15]))
                            climaObj.__setitem__("temperaturaSuperficie",float(datosArr[37]))
                            climaObj.__setitem__("temperaturaInternaPuntoRocioDL",float(datosArr[29]))
                            climaObj.__setitem__("temperaturaCalentamientoDL",float(datosArr[30]))
                            climaObj.__setitem__("temperaturaCalentamiento",float(datosArr[25]))
                            climaObj.__setitem__("temperaturaEnfriamiento",float(datosArr[26]))
                            climaObj.__setitem__("temperaturaInternaDL",float(datosArr[27]))
                            climaObj.__setitem__("temperaturaSensorAdicional",float(datosArr[33]))
                            climaObj.__setitem__("humedadExterior",datosArr[5])
                            climaObj.__setitem__("humedadRelativaSensorAdicional",datosArr[34])
                            climaObj.__setitem__("humedadInternaDL",int(datosArr[28]))
                            climaObj.__setitem__("humedadEquilibrioContenido",datosArr[31])
                            climaObj.__setitem__("humedadSuperficie",datosArr[36])
                            climaObj.__setitem__("puntoRocio",datosArr[6])
                            climaObj.__setitem__("vientoVelocidad",datosArr[7])
                            climaObj.__setitem__("vientoDireccion",datosArr[8])
                            climaObj.__setitem__("vientoRecorrido",datosArr[9])
                            climaObj.__setitem__("vientoVelocidadMaxima",datosArr[10])
                            climaObj.__setitem__("vientoDireccionMaxima",datosArr[11])
                            climaObj.__setitem__("vientoVelocidadMuestrasTiempo",int(datosArr[38]))
                            climaObj.__setitem__("presionBarometrica",datosArr[16])
                            climaObj.__setitem__("precipitacionAcumulada",datosArr[17])
                            climaObj.__setitem__("precipitacionIntensidad",datosArr[18])
                            climaObj.__setitem__("solarRadiacion",datosArr[19])
                            climaObj.__setitem__("solarEnergia",datosArr[20])
                            climaObj.__setitem__("solarEnergiaMaximo",datosArr[21])
                            climaObj.__setitem__("solarRadiacionIndiceExpoUV",datosArr[22])
                            climaObj.__setitem__("solarDosisEritematicaMinima",datosArr[23])
                            climaObj.__setitem__("solarRadiacionIndiceExpMaxIndiceUV",datosArr[24])
                            climaObj.__setitem__("aireDensidadInternaDL",datosArr[32])
                            climaObj.__setitem__("evapotranspiracionPotencial",datosArr[35])
                            climaObj.__setitem__("canalTransmisionDatosRF",int(datosArr[39]))
                            climaObj.__setitem__("canalRecepcionRF_ISS",datosArr[40])
                            climaObj.__setitem__("intervalosRecoleccionInformacion",int(datosArr[41]))
                            climaObj.__setattr__("fichero",file)
                            objetos.append(climaObj)
                    # todo cambiar los destino por arreglo
                    # os.rename(current_file,self.getCaminoDestino()+file)
                else:
                    # print "Fichero duplicado" + file
                    self.ficherosR.append(file)
                    # os.rename(current_file,self.getCaminoDuplicados()+file)
        del contenido,datosArr
        return objetos