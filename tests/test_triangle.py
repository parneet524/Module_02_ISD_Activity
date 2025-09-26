"""This module defines the TestTriangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = "Parneet kaur"
__version__ = "1.0.0"

import unittest
from shape import Triangle

class TestTriangle(unittest.TestCase):
    def setUp(self):
        # Common valid object for string/area/perimeter tests
        self.tri_567 = Triangle("red", 5, 6, 7)

    # __init__ validations
    def test_init_valid(self):
        t = Triangle("red", 5, 6, 7)
        self.assertIsInstance(t, Triangle)

    def test_blank_color_raises(self):
        with self.assertRaisesRegex(ValueError, "Color cannot be blank."):
            Triangle("   ", 5, 6, 7)

    def test_side1_not_int_raises(self):
        with self.assertRaisesRegex(ValueError, "Side 1 must be numeric."):
            Triangle("red", 5.2, 6, 7)

    def test_side2_not_int_raises(self):
        with self.assertRaisesRegex(ValueError, "Side 2 must be numeric."):
            Triangle("red", 5, "6", 7)

    def test_side3_not_int_raises(self):
        with self.assertRaisesRegex(ValueError, "Side 3 must be numeric."):
            Triangle("red", 5, 6, None)

    def test_triangle_inequality_raises(self):
        with self.assertRaisesRegex(ValueError, "The sides do not satisfy the Triangle Inequality Theorem."):
            Triangle("red", 1, 2, 3)

    # __str__
    def test_str_contains_color_and_sides(self):
        s = str(self.tri_567)
        self.assertIn("The shape color is red.", s)
        self.assertIn("5, 6 and 7", s)

    # calculate_area (Heron's formula)
    def test_area_for_345_triangle(self):
        t = Triangle("blue", 3, 4, 5)
        self.assertAlmostEqual(t.calculate_area(), 6.0, places=5)

    # calculate_perimeter
    def test_perimeter_sum_of_sides(self):
        t = Triangle("green", 2, 3, 4)
        self.assertEqual(t.calculate_perimeter(), 9.0)

if __name__ == "__main__":
    unittest.main()

