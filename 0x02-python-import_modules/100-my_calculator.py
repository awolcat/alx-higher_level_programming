#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    if operator == '+':
        result = calc.add(a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
    elif operator == '/':
        result = calc.div(a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
    elif operator == '*':
        result = calc.mul(a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
    elif operator == '-':
        result = calc.sub(a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
