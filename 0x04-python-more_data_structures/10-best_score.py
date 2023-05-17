#!/usr/bin/python3
def best_score(a_dictionary):
    number = 0
    student_list = []
    if a_dictionary is not None:
        for key in a_dictionary:
            if a_dictionary[key] > number:
                number = a_dictionary[key]
                student_list.append(key)
        return student_list[-1]
    else:
        return None
