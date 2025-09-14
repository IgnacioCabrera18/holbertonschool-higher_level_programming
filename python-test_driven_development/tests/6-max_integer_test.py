#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)
    
    def test_max_at_begginning(self):
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)
    
    def test_unordered_list(self):
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)
    
    def test_empty_list(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_only_one(self):
        one = [4]
        self.assertEqual(max_integer(one), 4)

    def test_floats(self):
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)
    
    def test_negative(self):
        negative = [-1, -2, -3, -4]
        self.assertEqual(max_integer(negative), -1)

if __name__ == '__main__':
    unittest.main()
