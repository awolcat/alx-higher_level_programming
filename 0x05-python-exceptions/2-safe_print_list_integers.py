#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    value = 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
            index += 1
            value += 1
        except (ValueError, TypeError):
            index += 1
            continue
    print()
    return value
