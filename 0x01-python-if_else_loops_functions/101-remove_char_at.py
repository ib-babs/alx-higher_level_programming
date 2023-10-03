#!/usr/bin/python3
def remove_char_at(str, n):
    idx = 0
    arr = [0] * 1024
    for l in str:
        arr[idx] = l
        idx += 1
    arr = arr[:idx]
    return arr
print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
