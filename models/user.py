#!/usr/bin/python3
""""user module"""
from models.base_model import BaseModel


class User (BaseModel):
    """user class"""
    first_name = ""
    email = ""
    last_name = ""
    password = ""
