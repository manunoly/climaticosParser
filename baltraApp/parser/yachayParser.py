__author__ = 'manuel'
from parser import parserGeneral
import os
from mongomodels import *
from datetime import datetime

class yachay(parserGeneral):
    ficheros = []
    def parser(self):
        path = self.getCaminoOrigen()
        dirs = os.listdir(path)
        objetos = []
        contenidoF = []
        for file in dirs:
            if (file.endswith('.dat')):
                self.ficheros.append(file)
                current_file = os.path.join(path, file)
                data = open(current_file,'r')
                contenido = data.readlines()
                contenidoF = contenidoF + contenido[4:]
                data.close()
        # i = 0
        # l = reduce(lambda x, y: x if y in x else x + [y], l, [])
        # contenidoA = contenido[1].split(",")
        # for conten in contenidoA:
        #     print (str(i) + "----" + conten)
        #     i+=1
        for line in list(set(contenidoF)):
            datosArr = line.replace('"NAN"',"-9999").split(",")

            fecha = datetime.strptime(datosArr[0].replace('"',''), '%Y-%m-%d %H:%M:%S')
            existeF = Clima.objects(Q(record=int(datosArr[1])) & Q(fecha=fecha)).count()
            if(existeF==0):
                climaObj = Clima()
                climaObj.__setitem__("Estacion","Yachay")
                # string_date = "2013-09-28 20:30:55.78200"
                climaObj.__setitem__("fecha", fecha)
                climaObj.__setitem__("record",int(datosArr[1]))
                climaObj.__setitem__("voltajeMinimoBateria",float(datosArr[2]))
                climaObj.__setitem__("temperaturaAirePromedio",float(datosArr[3]))
                climaObj.__setitem__("humedadAirePromedio",float(datosArr[4]))
                climaObj.__setitem__("vientoVelocidadPromedio",float(datosArr[5]))
                climaObj.__setitem__("vientoDireccionPromedio",float(datosArr[6]))
                climaObj.__setitem__("radiacioSolarPromedioW",float(datosArr[7]))
                climaObj.__setitem__("radiacioSolarPromedioMJ",float(datosArr[8]))
                climaObj.__setitem__("presionBarometricaPromedio",float(datosArr[9]))
                climaObj.__setitem__("nivelSonidoInternoPromedio",float(datosArr[10]))
                climaObj.__setitem__("nivelSonidoInternoExterno",float(datosArr[11]))
                climaObj.__setitem__("iluminacion3Promedio",float(datosArr[12]))
                climaObj.__setitem__("iluminacion7Promedio",float(datosArr[13]))
                climaObj.__setitem__("iluminacion7Promedio",float(datosArr[14]))
                climaObj.__setitem__("dioxidoCarbono3Promedio",float(datosArr[15]))
                climaObj.__setitem__("dioxidoCarbono6Promedio",float(datosArr[16]))
                climaObj.__setitem__("dioxidoCarbono7Promedio",float(datosArr[17]))
                climaObj.__setitem__("termocuplaPromedio1",float(datosArr[18]))
                climaObj.__setitem__("termocuplaPromedio2",float(datosArr[19]))
                climaObj.__setitem__("termocuplaPromedio3",float(datosArr[20]))
                climaObj.__setitem__("termocuplaPromedio4",float(datosArr[21]))
                climaObj.__setitem__("termocuplaPromedio5",float(datosArr[22]))
                climaObj.__setitem__("termocuplaPromedio6",float(datosArr[23]))
                climaObj.__setitem__("termocuplaPromedio7",float(datosArr[24]))
                climaObj.__setitem__("termocuplaPromedio8",float(datosArr[25]))
                climaObj.__setitem__("termocuplaPromedio9",float(datosArr[26]))
                climaObj.__setitem__("termocuplaPromedio10",float(datosArr[27]))
                climaObj.__setitem__("termocuplaPromedio11",float(datosArr[28]))
                climaObj.__setitem__("termocuplaPromedio12",float(datosArr[29]))
                climaObj.__setitem__("termocuplaPromedio13",float(datosArr[30]))
                climaObj.__setitem__("termocuplaPromedio14",float(datosArr[31]))
                climaObj.__setitem__("termocuplaPromedio15",float(datosArr[32]))
                climaObj.__setitem__("termocuplaPromedio16",float(datosArr[33]))
                climaObj.__setitem__("termocuplaPromedio17",float(datosArr[34]))
                climaObj.__setitem__("termocuplaPromedio18",float(datosArr[35]))
                climaObj.__setitem__("termocuplaPromedio19",float(datosArr[36]))
                climaObj.__setitem__("termocuplaPromedio20",float(datosArr[37]))
                climaObj.__setitem__("termocuplaPromedio21",float(datosArr[38]))
                climaObj.__setitem__("termocuplaPromedio22",float(datosArr[39]))
                climaObj.__setitem__("termocuplaPromedio23",float(datosArr[40]))
                climaObj.__setitem__("termocuplaPromedio24",float(datosArr[41]))
                climaObj.__setitem__("termocuplaPromedio25",float(datosArr[42]))
                climaObj.__setitem__("termocuplaPromedio26",float(datosArr[43]))
                climaObj.__setitem__("termocuplaPromedio27",float(datosArr[44]))
                climaObj.__setitem__("termocuplaPromedio28",float(datosArr[45]))
                climaObj.__setitem__("termocuplaPromedio29",float(datosArr[46]))
                climaObj.__setitem__("termocuplaPromedio20",float(datosArr[47]))
                climaObj.__setitem__("termocuplaPromedio31",float(datosArr[48]))
                climaObj.__setitem__("termocuplaPromedio32",float(datosArr[49]))
                # print datosArr.__len__()
                if(datosArr.__len__() > 50):
                    climaObj.__setitem__("dioxidocarbono3V",float(datosArr[50]))
                    climaObj.__setitem__("dioxidocarbono6V",float(datosArr[51]))
                    climaObj.__setitem__("dioxidocarbono7V",float(datosArr[52]))
                objetos.append(climaObj)

        del contenido
        del contenidoF
        return objetos
# "TIMESTAMP","RECORD","BattV_Min","TempAir_Avg","HumAir_Avg","WindVelocity_Avg","WindDirection_Avg","SlrW_Avg","SlrMJ_Tot","Barometric_Avg","SoundLevelIn_Avg","SoundLevelOut_Avg","Light3_Avg","Light6_Avg","Light7_Avg","CO2_3_Avg","CO2_6_Avg","CO2_7_Avg","Termocuple_Avg(1)","Termocuple_Avg(2)","Termocuple_Avg(3)","Termocuple_Avg(4)","Termocuple_Avg(5)","Termocuple_Avg(6)","Termocuple_Avg(7)","Termocuple_Avg(8)","Termocuple_Avg(9)","Termocuple_Avg(10)","Termocuple_Avg(11)","Termocuple_Avg(12)","Termocuple_Avg(13)","Termocuple_Avg(14)","Termocuple_Avg(15)","Termocuple_Avg(16)","Termocuple_Avg(17)","Termocuple_Avg(18)","Termocuple_Avg(19)","Termocuple_Avg(20)","Termocuple_Avg(21)","Termocuple_Avg(22)","Termocuple_Avg(23)","Termocuple_Avg(24)","Termocuple_Avg(25)","Termocuple_Avg(26)","Termocuple_Avg(27)","Termocuple_Avg(28)","Termocuple_Avg(29)","Termocuple_Avg(30)","Termocuple_Avg(31)","Termocuple_Avg(32)","co2_3v_Avg","co2_6v_Avg","co2_7v_Avg"