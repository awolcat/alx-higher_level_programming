#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    new_list = []
    [new_list.append(x) for x in my_list]
    new_list = list(set(new_list))
    for x in new_list:
        total += x
    return total
