#!/usr/bin/env python

class BinarySearch():

    def recursive_chop(self, position, target, array):
        if len(array) == 0:
            return -1
        if len(array) > 1:
            first_array = array[:len(array)/2] 
            second_array = array[len(array)/2:]
            first_result = self.recursive_chop(position, target, first_array)
            second_result = self.recursive_chop(position + len(array)/2, target, second_array)

            if (first_result != -1):
                return first_result
            elif (second_result !=-1):
                return second_result
            else:
                return -1

        else:
            if array[0] == target:
                return position
            else:
                return -1      

    

    def chop(self, target, array):
        return self.recursive_chop(0, target, array)
