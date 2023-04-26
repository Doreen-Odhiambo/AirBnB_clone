#!/usr/bin/python3
''' City class inheriting from BaseModel '''

from models.base_model import BaseModel


class City(BaseModel):
    ''' public class attributes '''
    # Define city to search
    state_id = ""
    name = ""
