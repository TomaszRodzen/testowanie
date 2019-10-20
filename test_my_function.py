import unittest


import my_functions


class TestAdd(unittest.TestCase):
    def test_add_integer(self):
        self.assertEqual(my_functions.add(3, 4), 7)
        self.assertEqual(my_functions.add(-4, -6), -10)

    def test_add_float(self):
        self.assertAlmostEqual(my_functions.add(3.2, 4.7), 7.9)
        self.assertAlmostEqual(my_functions.add(-1.7, 3.9), 2.2)

    def test_add_string(self):
        self.assertEqual(my_functions.add('ab', 'cd'), 'abcd')
        self.assertEqual(my_functions.add('', ''), '')


class TestDivide(unittest.TestCase):
    def test_value_error(self):
        self.assertRaises(ValueError, my_functions.divide, 3, 0)
        self.assertRaises(ValueError, my_functions.divide, 0, 0)


if __name__ == '__main__':
    unittest.main()

    """zadanie domowe zrob 100% coverage"""