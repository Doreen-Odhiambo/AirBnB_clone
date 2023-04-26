#!/usr/bin/python3
'''FileStorage class that serializes instances into a JSON file and
deserialize a JSON file into instances'''

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


date = {"BaseModel": BaseModel, "User": User, "State": State,
        "Place": Place, "City": City, "Amenity": Amenity, "Review": Review}


class FileStorage:
    '''Class that manages model storage
        hbnb in JSON format'''
    # string: path to the JSON file
    __file_path = "file.json"
    # dictionary - empty
    __objects = {}

    def all(self):
        ''' Returns the __objects dictionary '''
        return FileStorage.__objects

    def new(self, obj):
        ''' sets to __objects the obj with the key <obj class name>.id'''
       # Will store all objects by <class name>.id
        # eg to store a BaseModel object with id = 12121212,
        # the key will be BaseModel.12121212
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        ''' Serialize __objects into the JSON file (path: __file_path)'''
        dic_obj = {}
        # Write operation:
        # Create the json file where the information to be serialized will be stored
        with open(self.__file_path, "w", encoding="utf-8") as f:
            # Loop through the entered values
            for key, value in self.__objects.items():
                # I assign the value to the dic_obj in its keye
                dic_obj[key] = value.to_dict()
                # Convert Python objects to proper json objects
                # to be stored in a file
            json.dump(dic_obj, f)

    def reload(self):
        '''
        Deserialize the JSON file to __objects
        (only if the JSON file (__file_path) exists, otherwise
        if the file does not exist, no exception should be thrown)
        '''
        try:
            
             # read operation:
            # open the file for reading
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                # The file is deserialized
                j_dic = json.load(f)
            # The contents of the deserialized file are traversed
            for key in j_dic:
                value = date[j_dic[key]["__class__"]](**j_dic[key])
                # Sets the new values ​​of the object
                self.__objects[key] = value
        # Raised when a file or directory is requested but does not exist
        except FileNotFoundError:
            pass
