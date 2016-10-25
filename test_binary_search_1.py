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



if __name__ == '__main__':
    unittest.main()
