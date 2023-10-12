#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    unique = []
    for i in my_list:
        if i not in unique:
            sum += i
            unique.append(i)
    return sum
