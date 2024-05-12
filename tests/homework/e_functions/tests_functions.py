import unittest
from src.homework.e_functions.value_return import get_hour
from src.homework.e_functions.value_return import get_minutes
from src.homework.e_functions.value_return import get_seconds
class Test_Config(unittest.TestCase):

    def get_number_1(self):
        self.assertEqual(1, get_hour(3800))

    def get_number_2(self):
        self.assertEqual(1, get_hour(3600))

    def get_number_3(self):
        self.assertEqual(3, get_minutes(3800))

    def get_number_4(self):
        self.assertEqual(0, get_minutes(3600))

    def get_number_5(self):
        self.assertEqual(20, get_seconds(3800))

    def get_number_6(self):
        self.assertEqual(0, get_seconds(3600))
