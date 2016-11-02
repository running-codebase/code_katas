#!/usr/bin/env python

import unittest
from binary_search_3 import BinarySearch

class UnitTestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.bs = BinarySearch()
        self.array = [1, 2, 3, 4, 5]   

    def test_find_first_element(self):
        self.assertEquals(0, self.bs.chop(1, self.array))

    def test_find_last_element(self):
        self.assertEquals(4, self.bs.chop(5, self.array))

    def test_non_existent_element(self):
        self.assertEquals(-1, self.bs.chop(10, self.array))

    def test_all(self):
      self.assertEquals(-1, self.bs.chop(3, []))
      self.assertEquals(-1, self.bs.chop(3, [1]))
      self.assertEquals(0,  self.bs.chop(1, [1]))
      #
      self.assertEquals(0,  self.bs.chop(1, [1, 3, 5]))
      self.assertEquals(1,  self.bs.chop(3, [1, 3, 5]))
      self.assertEquals(2,  self.bs.chop(5, [1, 3, 5]))
      self.assertEquals(-1, self.bs.chop(0, [1, 3, 5]))
      self.assertEquals(-1, self.bs.chop(2, [1, 3, 5]))
      self.assertEquals(-1, self.bs.chop(4, [1, 3, 5]))
      self.assertEquals(-1, self.bs.chop(6, [1, 3, 5]))
      #
      self.assertEquals(0,  self.bs.chop(1, [1, 3, 5, 7]))
      self.assertEquals(1,  self.bs.chop(3, [1, 3, 5, 7]))
      self.assertEquals(2,  self.bs.chop(5, [1, 3, 5, 7]))
      self.assertEquals(3,  self.bs.chop(7, [1, 3, 5, 7]))
      self.assertEquals(-1, self.bs.chop(0, [1, 3, 5, 7]))
      self.assertEquals(-1, self.bs.chop(2, [1, 3, 5, 7]))
      self.assertEquals(-1, self.bs.chop(4, [1, 3, 5, 7]))
      self.assertEquals(-1, self.bs.chop(6, [1, 3, 5, 7]))
      self.assertEquals(-1, self.bs.chop(8, [1, 3, 5, 7]))
    
if __name__ == '__main__':
    unittest.main()
