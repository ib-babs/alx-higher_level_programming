#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    mul = 0
    sum_t = 0
    for i in my_list:
        mul += (i[0] * i[1])
        sum_t += i[1]
    return mul / sum_t
