#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        for index in range(len(my_list)):
            if idx != index:
                new_list.append(my_list[index])
            else:
                new_list.append(element)
        return new_list
