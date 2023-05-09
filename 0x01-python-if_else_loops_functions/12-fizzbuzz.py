#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        temp = i
        if i % 3 == 0:
            temp = "Fizz"
        if i % 5 == 0:
            temp = "Buzz"
        if i % 3 == 0 and i % 5 == 0:
            temp = "FizzBuzz"
        print("{}".format(temp), end=' ')
