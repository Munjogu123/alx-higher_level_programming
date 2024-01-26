#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_unorderedList(self):
        result = max_integer([1, 5, 4, 3, 2])
        self.assertEqual(result, 5)

    def test_emptyList(self):
        result = max_integer([])
        self.assertEqual(result, None)

    def test_orderedList(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_string(self):
        result = max_integer("Arbitrary")
        self.assertEqual(result, 'y')

    def test_oneElementList(self):
        result = max_integer([6])
        self.assertEqual(result, 6)

    def test_floatElements(self):
        result = max_integer([2.5, 3.7, 9.85, 7.78])
        self.assertEqual(result, 9.85)

    def test_negativeValues(self):
        result = max_integer([-2, -7, -1, -8, -10])
        self.assertEqual(result, -1)

    def test_negativeFloatValues(self):
        result = max_integer([-2.56, -7.57, -1.32, -8.14, -10.28])
        self.assertEqual(result, -1.32)

    def test_intAndFloats(self):
        result = max_integer([11, 2.34, 21, 9.80])
        self.assertEqual(result, 21)
