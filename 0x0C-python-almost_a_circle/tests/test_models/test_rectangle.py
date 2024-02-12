#!/usr/bin/python3"
""" Tests class Rectangle """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_instatiation(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

if __name__ == '__main__':
    unittest.main()
