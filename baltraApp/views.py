import json
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from array import *
from baltraApp.parser.mongomodels import *
import json

connect("clima")

class C(): pass

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError, e:
    return False
  return True

def index(request):
    return render(request, 'baltraApp/index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def contacto(request):
    # return True
    # contexto = Clima
    return render(request, 'baltraApp/contacto.html')

def iner(request):
    # return True
    # contexto = Clima
    return render(request, 'baltraApp/iner.html')

def mostrarDatos(request):
    # return True
    # contexto = Clima
    return render(request, 'baltraApp/mostrarDatos.html')

def reporteGeneral(request):
    # return True
    # contexto = Clima
    return render(request, 'baltraApp/reporteGeneral.html')

def estacionesCampos(request):
    estaciones = Estacion.objects
    datos = []

    for estacion in estaciones:
        obj = Clima.objects[:1].filter(Estacion=estacion.estacion).exclude("id", "fichero","fecha")
        datos.append(obj[0].__dict__)

    # exit()
            # .to_json(sort_keys=True)
    # for k in datos.keys():
    #     if k.startswith('s_'):
    #         del datos[k]
    # datos = Clima.objects[:2].filter(Estacion="BALTRA").only("id","Estacion","fecha").to_json()
    # return HttpResponse(datos)
    return HttpResponse(json.dumps(datos,sort_keys=True))


def graficaCampos():
    # for campo in request.GET.getlist["campos[]"]:
    #     fila = campo
    campos = []
    # if ('campos' in request.GET):
    #     campos = request.GET["campos"].split(",")
    #     campos.sort()
    camposFiltrar = "fecha"
    print type (camposFiltrar)
    print camposFiltrar
        # campoT = campos[0].split("_")[0]
        # for campo in campos:
            # if(campoT == campo.split("_")[0]):
            # camposFiltrar = camposFiltrar + '"' + campo.split("_")[1] + '",'
            # else:
        # resultado = Clima.objects[:5].filter(Estacion = campos[0].split("_")[0]).only('fecha: { $dateToString: { format: "%Y-%m-%d", fecha: "$date" } }')
    camposFiltro = "fecha, humedadRelativaMinima"
    resultado = Clima.objects[:2].filter(Estacion = "BALTRA").only(camposFiltrar).to_json()
            # campoT == campo.split("_")[0]
        # camposFiltrar = '"' + campo.split("_")[1] + '",'
            # if (i == campos.__len__()):
            #     resultado = resultado + Clima.objects.filter(Estacion=campoT).only(camposFiltrar[:camposFiltrar.__len__()-1])
            # else: i +=1
    # cada min q espero se ponen los psj +caros, ya lo he comprobado, lo voy a sacar y listo tengo miedo para cuando sacar psj porque despues q xavi tenga visa tiene un tiempo limite para entrar

    # else:return HttpResponse("Sin datos")

    return resultado

def cargarDatos(request):

    # datos = '{ "data": [["Name":"Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Name":"Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"],["Tiger Nixon","System Architect","Edinburgh","5421","2011/04/25","$320,800"],["Donna Snider","Customer Support","New York","4226","2011/01/25","$112,000"]]}'
    # datos = '{ "data": [{"chi":"Asdasd.0","Name":"Tiger Nixon","Position":"System Architect","Office":"Edinburgh","Extn":"5421","Startdate":"2011/04/25","Salary":"$320,800"},{"chi":"Asdasd","Name":"Tiger Nixon","Position":"System Architect","Office":"Edinburgh","Extn":"5421","Startdate":"2011/04/25","Salary":"$320,800"}]}'    # datos = Clima.objects.to_json()
    arreglo = []
    datos = Clima.objects[:15].to_json()
    # for dato in datos:
    #     objTemp = C
    #     objTemp.presionBarometricaMaxima = dato.presionBarometricaMaxima
    #     objTemp.vientoVelocidadPromedio = str(dato.vientoVelocidadPromedio)
    #     objTemp.radiacionSolarDifusaSumatoria = str(dato.radiacionSolarDifusaSumatoria)
    #     objTemp.vientoHoraRacha = str(dato.vientoHoraRacha)
    #     objTemp.vientoDireccionMaxima = str(dato.vientoDireccionMaxima)
    #     objTemp.vientoDireccionRachaMaxima = str(dato.vientoDireccionRachaMaxima)
    #     arreglo.append(objTemp.__dict__)
    # datos = json.dumps(arreglo)
    datos = datos.replace("[{",'{"data": [{') + "}"
    return HttpResponse(datos)

# def temperaturaJson(request,parameter):
#     if(parameter=="tap"):
#         datos = '[[20150128050401,22],[20150128050401,15],[20150128050403,8],[20150128050404,3],[20150128050405,17],[20150128050406,1],[20150128050407,19],[8,1],[20150128050409,15],[10,22],[11,12]]'
#     elif(parameter == "tamax"):
#         datos = '[[20150128050401,5],[20150228050401,18],[20150128050403,13],[20150128050404,7],[20150128050405,4],[20150128050406,9],[7,10],[20150128050408,15],[20150128050409,22],[10,31]]'
#     elif(parameter=="tamin"):
#         datos = '[[20150128050401,5],[20150228050401,11],[20150128050403,12],[20150128050404,17],[20150128050405,14],[20150128050406,19],[7,12],[20150128050408,14],[20150128050409,21],[10,9],[15,19],[18,31]]'
#     # datos =  '[{"name" : "AAPL","id":"dataseries","data" :[[1141171200000,69.10],[1141257600000,69.61],[1141344000000,67.72]"tooltip": {"yDecimals": 2}},{"type": "flags","name": "Flags on axis","onSeries": "dataseries","data": [{"x": 1143417600000,"title": "On axis"}],"shape": "squarepin"}]'
#     return HttpResponse(datos)

def temperaturaJson(request):
    datos = Clima.objects[:15].filter(Estacion="BALTRA").only("temperaturaAirePromedio","temperaturaAireMaxima","temperaturaAireMinima","fecha").order_by('+fecha')
    tempJs = '[{"name": "fecha","data": '
    fecha = []
    tempMax = []
    tempMin = []
    tempP = []
    for climaObj in datos:
        tempMax.append(str(climaObj.temperaturaAireMaxima))
        tempMin.append(str(climaObj.temperaturaAireMinima))
        tempP.append(str(climaObj.temperaturaAirePromedio))
        fecha.append(str(climaObj.fecha))
    # tempMin[len(tempMin)-1] = tempMin[len(tempMin)-1][:-1]
    # tempP[len(tempP)-1] = tempP[len(tempP)-1][:-1]
    # tempMax[len(tempMax)-1] = tempMax[len(tempMax)-1][:-1]
    # fecha[len(fecha)-1] = fecha[len(fecha)-1][:-1]
    fecha = str(fecha)
    fecha = fecha.replace("'",'"')
    tempMax = str(tempMax)
    tempMax = tempMax.replace("'",'')
    tempMin = str(tempMin)
    tempMin = tempMin.replace("'",'')
    tempP = str(tempP)
    tempP = tempP.replace("'",'')
    tempJs = tempJs + fecha + '}, {"name": "tempMax","data": ' + tempMax + '}, {"name": "tempMin","data": ' + tempMin + '}, {"name": "tempP","data": ' + tempP + '}]'
    return HttpResponse(tempJs)
    # return HttpResponse('[{"name": "Month","data": ["2015-10-01", "2015-10-02", "2015-10-03", "2015-10-04", "2015-10-05", "2015-10-06", "2015-10-06", "2015-10-07", "2015-10-080", "2015-10-09", "2015-10-10", "2015-10-11"]}, {"name": "Revenue","data": [23987, 24784, 25899, 25569, 25897, 25668, 24114, 23899, 24987, 25111, 25899, 23221]}, {"name": "Overhead","data": [21990, 22365, 21987, 22369, 22558, 22987, 23521, 23003, 22756, 23112, 22987, 22897]}]')


def humedadJson(request):
    datos = Clima.objects[:15].filter(Estacion="BALTRA").only("humedadRelativaPromedio","humedadRelativaMaxima","humedadRelativaMinima","fecha").order_by('+fecha')
    hJs = '[{"name": "fecha","data": '
    fecha = []
    hMax = []
    hMin = []
    hP = []
    for climaObj in datos:
        hMax.append(str(climaObj.humedadRelativaMaxima))
        hMin.append(str(climaObj.humedadRelativaMinima))
        hP.append(str(climaObj.humedadRelativaPromedio))
        fecha.append(str(climaObj.fecha))
    fecha = str(fecha)
    fecha = fecha.replace("'",'"')
    hMax = str(hMax)
    hMax = hMax.replace("'",'')
    hMin = str(hMin)
    hMin = hMin.replace("'",'')
    hP = str(hP)
    hP = hP.replace("'",'')
    hJs = hJs + fecha + '}, {"name": "humedadRelativaMaxima","data": ' + hMax + '}, {"name": "humedadRelativaMinima","data": ' + hMin + '}, {"name": "humedadRelativaPromedio","data": ' + hP + '}]'
    return HttpResponse(hJs)

def presionBarometricaJson(request):
    datos = Clima.objects[:15].filter(Estacion="BALTRA").only("presionBarometricaPromedio","presionBarometricaMaxima","presionBarometricaMinima","fecha").order_by('+fecha')
    pbJs = '[{"name": "fecha","data": '
    fecha = []
    pbMax = []
    pbMin = []
    pbP = []
    for climaObj in datos:
        pbMax.append(str(climaObj.presionBarometricaMaxima))
        pbMin.append(str(climaObj.presionBarometricaMinima))
        pbP.append(str(climaObj.presionBarometricaPromedio))
        fecha.append(str(climaObj.fecha))
    fecha = str(fecha)
    fecha = fecha.replace("'",'"')
    pbMax = str(pbMax)
    pbMax = pbMax.replace("'",'')
    pbMin = str(pbMin)
    pbMin = pbMin.replace("'",'')
    pbP = str(pbP)
    pbP = pbP.replace("'",'')
    pbJs = pbJs + fecha + '}, {"name": "presionBarometricaMaxima","data": ' + pbMax + '}, {"name": "presionBarometricaMinima","data": ' + pbMin + '}, {"name": "presionBarometricaPromedio","data": ' + pbP + '}]'
    return HttpResponse(pbJs)
    # return HttpResponse('[{"name": "Month","data": ["2015-10-01", "2015-10-02", "2015-10-03", "2015-10-04", "2015-10-05", "2015-10-06", "2015-10-06", "2015-10-07", "2015-10-080", "2015-10-09", "2015-10-10", "2015-10-11"]}, {"name": "Revenue","data": [23987, 24784, 25899, 25569, 25897, 25668, 24114, 23899, 24987, 25111, 25899, 23221]}, {"name": "Overhead","data": [21990, 22365, 21987, 22369, 22558, 22987, 23521, 23003, 22756, 23112, 22987, 22897]}]')


def vientoJson(request):
    datos = Clima.objects[:15].filter(Estacion="BALTRA").only("vientoVelocidadPromedio","vientoVelocidadMaxima","vientoVelocidadMinima","fecha").order_by('+fecha')
    pbJs = '[{"name": "fecha","data": '
    fecha = []
    pbMax = []
    pbMin = []
    pbP = []
    for climaObj in datos:
        pbMax.append(str(climaObj.vientoVelocidadMaxima))
        pbMin.append(str(climaObj.vientoVelocidadMinima))
        pbP.append(str(climaObj.vientoVelocidadPromedio))
        fecha.append(str(climaObj.fecha))
    fecha = str(fecha)
    fecha = fecha.replace("'",'"')
    pbMax = str(pbMax)
    pbMax = pbMax.replace("'",'')
    pbMin = str(pbMin)
    pbMin = pbMin.replace("'",'')
    pbP = str(pbP)
    pbP = pbP.replace("'",'')
    pbJs = pbJs + fecha + '}, {"name": "vientoVelocidadMaxima","data": ' + pbMax + '}, {"name": "vientoVelocidadMinima","data": ' + pbMin + '}, {"name": "vientoVelocidadPromedio","data": ' + pbP + '}]'
    return HttpResponse(pbJs)