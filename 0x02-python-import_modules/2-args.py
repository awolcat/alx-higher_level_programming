#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    count = 1
    if args == 1:
        print("0 arguments.")
    elif args == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(args - 1))
        for i in argv:
            if i != argv[0]:
                print("{}: {}".format(count, i))
                count = count + 1
