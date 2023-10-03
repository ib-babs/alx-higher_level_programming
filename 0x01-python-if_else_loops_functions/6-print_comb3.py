#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if j < i or j == i:
            continue
        if j > 1:
            print(", ", end='')
        print(f"{i}{j}", end='')
print()
