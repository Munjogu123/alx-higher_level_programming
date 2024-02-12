#!/usr/bin/python3"
""" Defines unittest for the class Base """
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstatiation(unittest.TestCase):
    """ Tests the instatiation of the class Base """
    def test_noArgs(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)


if __name__ == '__main__':
    unittest.main()
