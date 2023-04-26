#!/usr/bin/python3
''' Class BaseModel '''

import models
from datetime import datetime
import uuid


class BaseModel:
    '''
    
    Base class that defines all
    common attributes/methods for other classes
    '''
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            # Loop through the key and value in the entered items
            for key, value in kwargs.items():
                # Assigns the key to the current creation date
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                # Assigns the key to the updated date
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
               # Assign the value to the key
                # self: The object whose attribute is to be assigned.
                # key: attribute of the object to be assigned.
                # value: value with which the variable will be assigned.
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            # Assign random id
            self.id = str(uuid.uuid4)
            # Assign current date
            self.created_at = datetime.now()
            # Update the date of the last modification
            self.updated_at = self.created_at
            # If it is a new instance
            # not from a dictionary representation
            models.storage.new(self)

    def __str__(self):
        '''returns the name of the class, the ID and
        the attribute dictionary '''
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''' update the public instance attribute
        updated_at with the current date and time'''
        self.updated_at = datetime.now()
        # call the save(self) method of storage
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all
        the __dict__ keys/values ​​of the instance'''
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic["__class__"] = self.__class__.__name__
        return dic
