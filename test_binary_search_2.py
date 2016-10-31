#!/usr/bin/env python

import unittest
from binary_search_2 import BinarySearch

class TestBinarySearch2(unittest.TestCase):

    def setUp(self):
        self.bs = BinarySearch()
        self.array = [1, 2, 3, 4, 5]
        
  
    def test_first_element(self):
        self.assertEquals(0, self.bs.chop(1, self.array))

    def test_last_element(self):
        self.assertEquals(4, self.bs.chop(5, self.array))

    def test_non_existing_element(self):
        self.assertEquals(-1, self.bs.chop(9, self.array))



if __name__ == '__main__':
    unittest.main()
