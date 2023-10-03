#!/usr/bin/python3
for i in range(0, 100):
    if (i < 10):
        i = "0" + str(i)
    if (i == 99):
        i = str(i) + "\n"
    print(f"{i}", end="")
    if (int(i) < 99):
        print(", ", end="")
