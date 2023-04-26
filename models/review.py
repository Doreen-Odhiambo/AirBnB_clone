#!/usr/bin/python3
''' Review class inheriting from BaseModel '''

from models.base_model import BaseModel


class Review(BaseModel):
    ''' public class attributes '''
    # Reviews made by users about a place
    place_id = ""
    user_id = ""
    text = ""
