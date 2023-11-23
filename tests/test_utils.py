import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *

class TestGetTotalNumberOfCells(unittest.TestCase):
    
    def test_small_value(self):
        self.assertEqual(get_total_number_of_cells(1), 3)
    
    def test_medium_value(self):
        self.assertEqual(get_total_number_of_cells(3), 9)
    
    def test_large_value(self):
        self.assertEqual(get_total_number_of_cells(5), 33)

class TestGetTotalNumberOfPossibleRules(unittest.TestCase):
    
    def test_small_value(self):
        self.assertEqual(get_total_number_of_possible_rules(1), 2**3)

    def test_medium_value(self):
        self.assertEqual(get_total_number_of_possible_rules(3), 2**9)

    def test_large_value(self):
        self.assertEqual(get_total_number_of_possible_rules(5), 2**33)

if __name__ == '__main__':
    unittest.main()
