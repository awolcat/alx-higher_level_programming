#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string != "" and roman_string != None:
        if len(roman_string) == 1:
            number = roman[roman_string[0]]
            return number
        if roman[roman_string[0]] < roman[roman_string[-1]]:
            number = roman[roman_string[-1]]
            for i in range(len(roman_string) - 1):
                number -= roman[roman_string[i]]
            return number
        elif roman[roman_string[0]] > roman[roman_string[-1]]:
            number = roman[roman_string[0]]
            for i in range(1, len(roman_string)):
                number += roman[roman_string[i]]
            return number
    else:
        return 0
