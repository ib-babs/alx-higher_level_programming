#!/usr/bin/python3
for x in range(ord('a'), ord('z') + 1):
    if x == 113 or  x == 101:
        continue
    print("{:c}".format(x), end='')
