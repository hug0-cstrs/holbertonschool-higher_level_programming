#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    copy = my_list[:]
    for i in my_list:
        if copy[i] % 2 == 0:
            copy[i] = True
        else:
            copy[i] = False
    return copy
