import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *

class TestGetTotalNumberOfCells(unittest.TestCase):
    
    def test_small_value(self):
        self.assertEqual(get_total_number_of_cells(0), 1)
    
    def test_medium_value(self):
        self.assertEqual(get_total_number_of_cells(1), 3)
    
    def test_large_value(self):
        self.assertEqual(get_total_number_of_cells(2), 5)

class TestGetTotalNumberOfPossibleRules(unittest.TestCase):
    
    def test_small_value(self):
        self.assertEqual(get_total_number_of_possible_rules(0), 4)

    def test_medium_value(self):
        self.assertEqual(get_total_number_of_possible_rules(1), 256)

    def test_large_value(self):
        self.assertEqual(get_total_number_of_possible_rules(2), 4294967296)

if __name__ == '__main__':
    unittest.main()
