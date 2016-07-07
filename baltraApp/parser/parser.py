__author__ = 'manuel'
from configuracionApp import configuracion

class parserGeneral():
    configuracionObj = configuracion()

    def getCaminoOrigen(self):
        path = getattr(self.configuracionObj,self.__class__.__name__+"Origen")
        return path

    def getCaminoDestino(self):
        path = getattr(self.configuracionObj,self.__class__.__name__+"Destino")
        return path

    def getCaminoDuplicados(self):
        path = getattr(self.configuracionObj,self.__class__.__name__+"Duplicados")
        return path
    def getLog(self):
        path = getattr(self.configuracionObj,self.__class__.__name__+"Log")
        return path
    def getError(self):
        path = getattr(self.configuracionObj,self.__class__.__name__+"Error")
        return path
    def getRaiz(self):
        path = getattr(self.configuracionObj,self.__class__.__name__+"Raiz")
        return path