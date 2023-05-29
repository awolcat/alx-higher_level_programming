#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    div = 0
    result = []
    while index < list_length:
        try:
            div = my_list_1[index] / my_list_2[index]
            result.append(div)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            index += 1
    return result
