#!/usr/bin/python3
''' Amenity class that inherits from BaseModel '''

from models.base_model import BaseModel


class Amenity(BaseModel):
    ''' Atributos de clase pública '''
    # Defines the conveniences that the user
    # can choose to offer instead
    name = ""
