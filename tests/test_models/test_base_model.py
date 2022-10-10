#!/usr/bin/python3
""""test file"""


from turtle import update
import unittest
from uuid import uuid4
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """"test base model"""

    def test_id(self):
        """"test id"""

        self.id1 = BaseModel()
        self.id2 = BaseModel()
        self.assertNotEqual(self.id1.id, self.id2.id)

    def test_save(self):
        ''''test save'''

        sa = BaseModel()
        sleep(0.1)
        update = sa.updated_at
        sa.save()
        self.assertLess(update, sa.updated_at)

    def test_to_dict(self):
        """"test dict"""
        bm = BaseModel()
        sleep(0.1)
        bm2 = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm2.to_dict())

    def test___str__(self):
        """
        test str 
        """
        bm = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm.__str__(), bm2.__str__())


if __name__ == '__main__':
    unittest.main()
