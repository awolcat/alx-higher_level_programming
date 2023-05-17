#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = a_dictionary 
    new_dict = sorted(new_dict)
    for key in new_dict:
        print("{}: {}".format(key, a_dictionary[key]))
