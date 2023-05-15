#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = None
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if largest == None or largest < i:
                largest = i
    return largest
