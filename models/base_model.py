#!/usr/bin/python3
""""base model"""

from datetime import datetime
from uuid import uuid4


class BaseModel():
    ''''base class'''

    def __init__(self):
        """"initialization"""

        self.id = str(uuid4())
        self.created_at = datetime.now
        self.updated_at = datetime.now

    def __str__(self):
        """"print"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''''updates the public instance attribute'''
        self.updated_at = datetime.now

    def to_dict(self):
        """"returns a dictionary containing all keys/values"""
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
