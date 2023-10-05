#!/usr/bin/python3

def print_args(argv):
    argv_len = len(argv)
    i = 1
    if argv_len == 1:
        print("0 argument.")
    elif argv_len == 2:
        print("1 argument:\n1: {:s}".format(argv[1]))
    else:
        print("{} arguments:".format(argv_len - 1))
        for arg in argv[1:]:
            print("{}: {:s}".format(i, arg))
            i = i + 1


if __name__ == "__main__":
    from sys import argv
    print_args(argv)
