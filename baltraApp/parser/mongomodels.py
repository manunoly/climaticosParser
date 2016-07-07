__author__ = 'manuel'

import mongoengine

from mongoengine import *


class Estacion(Document):
    estacion = StringField(max_length=50,required=True)
    ubicacion = StringField(max_length=120,required=True)


class Clima(DynamicDocument):
    datos = StringField()