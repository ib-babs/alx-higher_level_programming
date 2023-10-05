#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def arg_calc(argv):
    argv_len = len(argv)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    if argv_len != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    if operator == "+":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, add(a, b)))
    elif operator == "-":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, mul(a, b)))
    elif operator == "/":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import sys
    arg_calc(sys.argv)
