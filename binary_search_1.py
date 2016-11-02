#!/usr/bin/env python

class BinarySearch():
    def chop(self, value, array):
        if len(array) == 0:
            return -1
       
        i = 0
        k = len(array) - 1
        
        while k - i > 1:
            mid = i + (k - i) / 2
            if array[mid] == value:
                return mid
            elif array[mid] < value:
                i = mid
            else:
                k = mid


        if (value == array[i]):
            return i
        elif(value == array[k]):
            return k
        else:
            return -1
