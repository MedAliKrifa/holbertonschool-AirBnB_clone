#!/usr/bin/python3
""""file storage class"""

from ast import Pass
from models.base_model import BaseModel
import json
import os.path



class FileStorage:
    """"file storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """"returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """"sets in __objects the obj with key <obj class name>.id"""

        self.__objects["{}{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        ''''serializes __objects to the JSON file (path: __file_path)'''

        dic = {}

        for i in self.__objects:
            dic = i
            dic[i] = self.__objects[i]
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(dic, f)

    def reload(self):
        """deserializes the JSON file to __objects"""

        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                obj = json.load(f)

            for key, v in obj.items():
                self.__objects[key] = eval(v['__class__'])(**v)
        except FileNotFoundError:
            pass