import unittest
from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers
class Test_Config(unittest.TestCase):
    class Test_Config(unittest.TestCase):

        def test_get_factorial_1(self):
        #test that the function get_number returns 1
            self.assertEqual(24, get_factorial(4))
    
        def test_get_factorial_2(self):
        #test that the function get_number returns 2
            self.assertEqual(120, get_factorial(5))

        def test_get_factorial_3(self):
        #test that the function get_number returns 2
            self.assertEqual(720, get_factorial(6))

        def test_odd_sum_1(self):
        #test that the function get_number returns 2
            self.assertEqual(16, sum_odd_numbers(7))

        def test_odd_sum_2(self):
        #test that the function get_number returns 2
            self.assertEqual(25, sum_odd_numbers(9))

        def test_odd_sum_3(self):
        #test that the function get_number returns 2
            self.assertEqual(25, sum_odd_numbers(10))