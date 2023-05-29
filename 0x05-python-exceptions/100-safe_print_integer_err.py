#!/usr/bin/python3
def safe_print_integer_err(value):
    val = False
    try:
        print("{:d}".format(value))
        val = True
        return val
    except (TypeError, ValueError):
        raise Exception("Unknown format code 'd' for object of type 'str'") from None
    finally:
        return val
