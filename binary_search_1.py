#!/usr/bin/env python

import time 

class BinarySearch():
    def chop(self, value, array):
        i = 0
        k = len(array) - 1
        print "Start search for %s" %value
        
        while k - i > 1:
            mid = i + (k - i) / 2
#            print "i: %s , k: %s, mid: %s " %(i, k, mid)           
 
            if array[mid] == value:
                print "Mid was the correct value. Returning"
                return mid
            elif array[mid] < value:
#                print "Mid is less then: ", value 
                i = mid
            else:
#                print "Mid is greater then: ", value 
                k = mid

#            time.sleep(1)

        if (value == array[i]):
            print "Found value: ", i
            return i
        elif(value == array[i+1]):
            print "Found hacked value: ", i +1
            return i + 1
        else:
            print "Could not find: ", value
            return -1
