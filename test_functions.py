# test_functions.py

import unittest
from functions import greet, calculate_area, is_even, get_initials

class TestFunctions(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Dave"), "Hello, Dave!")

    def test_calculate_area(self):
        self.assertEqual(calculate_area(5, 3), 15)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))

    def test_get_initials(self):
        self.assertEqual(get_initials("John Doe"), "JD")

if __name__ == '__main__':
    unittest.main()
