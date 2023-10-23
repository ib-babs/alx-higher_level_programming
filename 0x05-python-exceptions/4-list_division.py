#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = None
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError as ZDE:
            result = 0
            print("division by 0")
        except TypeError as TE:
            result = 0
            print("wrong type")
        except IndexError as IE:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)

    return new_list
