#!/usr/bin/env python

#Functional implementation
class BinarySearch():

    def chop(self, target, array):
        if len(array) == 0:
            return -1
        i = 0
        k = len(array) - 1

        while (k-i >1): 
            half = i + (k-i)/2
            if array[half] == target:
                return half
            elif array[half] < target:
                i = half
            else:
                k = half


        if array[i] == target:
            return i
        elif array[k] == target:
            return k
        else:
            return -1

