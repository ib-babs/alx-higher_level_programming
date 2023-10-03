#!/usr/bin/python3
for letter in "abcdefghijklmnopqrstuvwxyz":
    if ('q' in letter) or ('e' in letter):
        continue
    print(f"{letter}", end="")
