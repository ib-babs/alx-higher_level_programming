#!/usr/bin/python3
i = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    letter = 122 - ord(letter) + 97
    if i % 2 == 1:
        letter = letter - 32
    print(f"{chr(letter)}", end="")
    i += 1
