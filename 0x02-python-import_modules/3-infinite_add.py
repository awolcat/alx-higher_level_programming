#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    for i in argv:
        if i != argv[0]:
            total = total + int(i)
    print(total)
