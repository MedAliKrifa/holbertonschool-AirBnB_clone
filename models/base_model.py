#!/usr/bin/python3
""""base model"""

from datetime import date, datetime
from uuid import uuid4
import models

class BaseModel:
    ''''base class'''

    def __init__(self, *args, **kwargs):
        """"initialization"""
        keyarl=len(kwargs)
        if keyarl > 0 :
            for k,v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'created_at' or k == 'updated_at':
                    setattr(self,k, datetime.fromisoformat(v))
                else:
                    setattr(self,k,v)
        else:
            self.id=str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """"print"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        ''''updates the public instance attribute'''
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """"returns a dictionary containing all keys/values"""
        
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
