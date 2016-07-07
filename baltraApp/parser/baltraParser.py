__author__ = 'manuel'

from mongomodels import *
import datetime
import os
from parser import parserGeneral
class baltra(parserGeneral):
    ficheros = []

    def parserBaltra(self):
        i = 0;
        # configuracionObj = configuracion("BALTRA")
        path = self.getCaminoOrigen()
        dirs = os.listdir(path)
        objetos = []
        for file in dirs:
            self.ficheros.append(file)
            if (file.endswith('.rep')):
                current_file = os.path.join(path, file)
                existeF = Clima.objects(fichero=file)
                if(existeF.__len__() == 0):
                    data = open(current_file,'r')
                    text = data.read()
                    text = str.replace(str.replace(text,"(",""),")","")
                    separadores = text.split(";")
                    estacion = separadores[0].split(":")
                    temperaturaAirePromedio = separadores[3].split(":")
                    temperaturaAireMaxima = separadores[4].split(":")
                    temperaturaAireMinima = separadores[5].split(":")

                    humedadRelativaPromedio = separadores[6].split(":")
                    humedadRelativaMaxima = separadores[7].split(":")
                    humedadRelativaMinima = separadores[8].split(":")

                    presionBarometricaPromedio = separadores[9].split(":")
                    presionBarometricaMaxima = separadores[10].split(":")
                    presionBarometricaMinima = separadores[11].split(":")

                    radiacionSolarGlobalPromedio = separadores[12].split(":")
                    radiacionSolarGlobalMaxima = separadores[13].split(":")
                    radiacionSolarGlobalMinima = separadores[14].split(":")
                    radiacionSolarGlobalSumatoria = separadores[15].split(":")

                    radiacionSolarDifusaPromedio = separadores[16].split(":")
                    radiacionSolarDifusaMaxima = separadores[17].split(":")
                    radiacionSolarDifusaMinima = separadores[18].split(":")
                    radiacionSolarDifusaSumatoria = separadores[19].split(":")

                    direccionVientoPromedio = separadores[20].split(":")
                    direccionVientoMaxima = separadores[21].split(":")
                    direccionRachaMaxima = separadores[22].split(":")
                    horaRacha = separadores[23].split(":")
                    minutoRacha = separadores[24].split(":")
                    velocidadVientoPromedio = separadores[25].split(":")
                    velocidadVientoMaxima = separadores[26].split(":")
                    velocidadViento = separadores[27].split(":")
                    recorridoViento = separadores[28].split(":")
                    voltajeBateria =  separadores[29].split(":")

                    fecha = separadores[1].split(":")
                    horaD = separadores[2].split(":")

                    anno = int(fecha[1][:2]) + 2000
                    mes = int(fecha[1][2:4])
                    dia = int(fecha[1][4:6])

                    hora = int(horaD[1][:2])
                    minuto = int(horaD[1][2:4])
                    seg = int(horaD[1][4:6])
                    i = i + 1

                    climaObj = Clima()
                    climaObj.__setitem__("Estacion",estacion[1])
                    climaObj.__setitem__("fecha", datetime.datetime(anno,mes,dia,hora,minuto,seg))

                    climaObj.temperaturaAirePromedio = float(temperaturaAirePromedio[1])
                    climaObj.temperaturaAireMaxima= float(temperaturaAireMaxima[1])
                    climaObj.temperaturaAireMinima = float(temperaturaAireMinima[1])

                    climaObj.humedadRelativaPromedio = int(humedadRelativaPromedio[1])
                    climaObj.humedadRelativaMaxima = int(humedadRelativaMaxima[1])
                    climaObj.humedadRelativaMinima = int(humedadRelativaMinima[1])

                    climaObj.presionBarometricaPromedio = float(presionBarometricaPromedio[1])
                    climaObj.presionBarometricaMaxima = float(presionBarometricaMaxima[1])
                    climaObj.presionBarometricaMinima = float(presionBarometricaMinima[1])

                    climaObj.radiacionSolarGlobalPromedio = int(radiacionSolarGlobalPromedio[1])
                    climaObj.radiacionSolarGlobalMaxima = int(radiacionSolarGlobalMaxima[1])
                    climaObj.radiacionSolarGlobalMinima = int(radiacionSolarGlobalMinima[1])
                    climaObj.radiacionSolarGlobalSumatoria = int(radiacionSolarGlobalSumatoria[1])
                    climaObj.radiacionSolarDifusaPromedio = int(radiacionSolarDifusaPromedio[1])

                    climaObj.radiacionSolarDifusaMaxima  = int(radiacionSolarDifusaMaxima[1])
                    climaObj.radiacionSolarDifusaMinima = int(radiacionSolarDifusaMinima[1])
                    climaObj.radiacionSolarDifusaSumatoria = int(radiacionSolarDifusaSumatoria[1])

                    climaObj.vientoDireccionPromedio = float(direccionVientoPromedio[1])
                    climaObj.vientoDireccionMaxima = float(direccionVientoMaxima[1])
                    climaObj.vientoDireccionRachaMaxima = float(direccionRachaMaxima[1])
                    climaObj.vientoHoraRacha = int(horaRacha[1])
                    climaObj.vientoMinutoRacha = int(minutoRacha[1])
                    climaObj.vientoVelocidadPromedio = float(velocidadVientoPromedio[1])
                    climaObj.vientoVelocidadMaxima = float(velocidadVientoMaxima[1])
                    climaObj.vientoVelocidadMinima = float(velocidadViento[1])
                    climaObj.vientoRecorrido = recorridoViento[1]

                    # climaObj.__setitem__("Temperatura",{ "temperaturaAirePromedio" : float(temperaturaAirePromedio[1]),"temperaturaAireMaxima":float(temperaturaAireMaxima[1]),"temperaturaAireMinima":float(temperaturaAireMinima[1])})
                    # climaObj.__setitem__("HumedadRelativa",{ "humedadRelativaPromedio" : float(humedadRelativaPromedio[1]), "humedadRelativaMaxima": float(humedadRelativaMaxima[1]),"humedadRelativaMinima":float(humedadRelativaMinima[1])})
                    # climaObj.__setitem__("PresionBarometrica",{ "presionBarometricaPromedio" : float(presionBarometricaPromedio[1]),"presionBarometricaMaxima": float(presionBarometricaMaxima[1]), "presionBarometricaMinima": float(presionBarometricaMinima[1])})
                    # climaObj.__setitem__("RadiacionSolarGlobal",{ "radiacionSolarGlobalPromedio" : float(radiacionSolarGlobalPromedio[1]), "radiacionSolarGlobalMaxima":float(radiacionSolarGlobalMaxima[1]), "radiacionSolarGlobalMinima": decimal.Decimal(radiacionSolarGlobalMinima[1]), "radiacionSolarGlobalSumatoria":float(radiacionSolarGlobalSumatoria[1])})
                    # climaObj.__setitem__("RadiacionSolarDifusa",{ "radiacionSolarDifusaPromedio" : float(radiacionSolarDifusaPromedio[1]),"radiacionSolarDifusaMaxima":float(radiacionSolarDifusaMaxima[1]), "radiacionSolarDifusaMinima": float(radiacionSolarDifusaMinima[1]), "radiacionSolarDifusaSumatoria": float(radiacionSolarDifusaSumatoria[1])})
                    # climaObj.__setitem__("DireccionViento",{ "direccionVientoPromedio" : float(direccionVientoPromedio[1]),"direccionVientoMaxima":float(direccionVientoMaxima[1]),"direccionRachaMaxima": float(direccionRachaMaxima[1]), "horaRacha": int(horaRacha[1]), "minutoRacha": int(minutoRacha[1]), "velocidadVientoPromedio":float(velocidadVientoPromedio[1]), "velocidadVientoMaxima": float(velocidadVientoMaxima[1]),"velocidadViento":float(velocidadViento[1]),"recorridoViento": recorridoViento[1] })

                    climaObj.__setitem__("voltajeBateria", float(voltajeBateria[1]))
                    climaObj.__setattr__("fichero",file)
                    objetos.append(climaObj)
                    os.rename(current_file, self.getCaminoDestino()+file)
                else:
                    os.rename(current_file, self.getCaminoDuplicados()+file)
        return objetos
