#!/usr/bin/env python

import unittest
from binary_search_1 import BinarySearch

class TestStringMethods(unittest.TestCase):

    def test_binary_search(self):
        bs = BinarySearch()
        array = [1, 2, 3, 4, 5]
        self.assertEquals(2, bs.chop(3, array))

    def test_not_in_set(self):
        bs = BinarySearch()
        array = [1, 2, 3, 4, 5]
        self.assertEquals(-1, bs.chop(6, array))

    def test_last_element(self):
        bs = BinarySearch()
        array = [1, 2, 3, 4, 5]
        self.assertEquals(4, bs.chop(5, array))

    def test_first_element(self):
        bs = BinarySearch()
        array = [1, 2, 3, 4, 5]
        self.assertEquals(0, bs.chop(1, array))

    def test_second_element(self):
        bs = BinarySearch()
        array = [1, 2, 3, 4, 5]
        self.assertEquals(1, bs.chop(2, array))

    def test_all(self):
        bs = BinarySearch()
        self.assertEquals(-1, bs.chop(3, []))
        self.assertEquals(-1, bs.chop(3, [1]))
        self.assertEquals(0,  bs.chop(1, [1]))
        #
        self.assertEquals(0,  bs.chop(1, [1, 3, 5]))
        self.assertEquals(1,  bs.chop(3, [1, 3, 5]))
        self.assertEquals(2,  bs.chop(5, [1, 3, 5]))
        self.assertEquals(-1, bs.chop(0, [1, 3, 5]))
        self.assertEquals(-1, bs.chop(2, [1, 3, 5]))
        self.assertEquals(-1, bs.chop(4, [1, 3, 5]))
        self.assertEquals(-1, bs.chop(6, [1, 3, 5]))
        #
        self.assertEquals(0,  bs.chop(1, [1, 3, 5, 7]))
        self.assertEquals(1,  bs.chop(3, [1, 3, 5, 7]))
        self.assertEquals(2,  bs.chop(5, [1, 3, 5, 7]))
        self.assertEquals(3,  bs.chop(7, [1, 3, 5, 7]))
        self.assertEquals(-1, bs.chop(0, [1, 3, 5, 7]))
        self.assertEquals(-1, bs.chop(2, [1, 3, 5, 7]))
        self.assertEquals(-1, bs.chop(4, [1, 3, 5, 7]))
        self.assertEquals(-1, bs.chop(6, [1, 3, 5, 7]))
        self.assertEquals(-1, bs.chop(8, [1, 3, 5, 7])) 

if __name__ == '__main__':
    unittest.main()
