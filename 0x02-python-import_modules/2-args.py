#!/usr/bin/python3

def print_args(argv):
    n = len(argv) - 1
    i = 1
    if n == 0:
        print("0 argument.")
    elif n == 1:
        print("{:d} argument:\n{:d}: {:s}".format(n, n, argv[1]))
    else:
        print("{} arguments:".format(n))
        for arg in argv[1:]:
            print("{}: {:s}".format(i, arg))
            i = i + 1


if __name__ == "__main__":
    from sys import argv
    print_args(argv)
