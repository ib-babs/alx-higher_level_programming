#!/usr/bin/python3
def infinite_num():
    from sys import argv
    sum = 0
    for arg in argv[1:]:
        sum = sum + int(arg)
    print(sum)


if __name__ == "__main__":
    infinite_num()
