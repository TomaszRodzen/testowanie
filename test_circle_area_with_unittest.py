import unittest


import math


import my_class


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        """test area when radius >=0"""
        self.assertAlmostEqual(my_class.circle_area(1), math.pi)
        self.assertAlmostEqual(my_class.circle_area(2.1), math.pi*(2.1**2))

    def test_values(self):
        self.assertRaises(ValueError, my_class.circle_area, -2)

    def test_types(self):
        self.assertRaises(TypeError, my_class.circle_area, 3+5j)
        self.assertRaises(TypeError, my_class.circle_area, True)
        self.assertRaises(TypeError, my_class.circle_area, 'radius')


if __name__ == "__main__":
    unittest.main()


