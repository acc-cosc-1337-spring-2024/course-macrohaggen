import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
from tests.homework.j_classes import tests_classes
suite = unittest.TestLoader().loadTestsFromModule(tests_classes)