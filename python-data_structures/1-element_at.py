#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None

    lenght = len(my_list) - 1

    if idx > lenght:
        return None

    return my_list[idx]
