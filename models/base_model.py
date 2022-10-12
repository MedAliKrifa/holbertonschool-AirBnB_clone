#!/usr/bin/python3
""""base model"""

from datetime import datetime
from uuid import uuid4
import models

class BaseModel():
    ''''base class'''

    def __init__(self, *args, **kwargs):
        """"initialization"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if (kwargs):
            for i in kwargs:
                if i == "created_at":
                    self.created_at = datetime.strptime(kwargs[i], '%Y-%m-%dT%H:%M:%S.%f').date()
                elif i == "updated_at":

                    self.updated_at = datetime.strptime(kwargs[i], '%Y-%m-%dT%H:%M:%S.%f').date()
                else:
                    self.id = str(kwargs[i])
        
            

    def __str__(self):
        """"print"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''''updates the public instance attribute'''
        self.updated_at = datetime.now()

    def to_dict(self):
        """"returns a dictionary containing all keys/values"""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()

        return dict
