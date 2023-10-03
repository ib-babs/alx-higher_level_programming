#!/usr/bin/python3
# 2-print_alphabet.py
# Babatunde Ibrahim

"""Print the alphabet in lwercase, not followed by a new line."""
for x in range(ord('a'), ord('z') + 1):
    print("{:c}".format(x), end='')
