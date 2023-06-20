#!/usr/bin/python3
"""A module with a class MyList that inherits from class list"""


class MyList(list):
    """ Class that inherits the attributes references of class list

    Args:
        list: class list

    """
    def print_sorted(self):
        """ Method that prints the sorted list """
        print(sorted(self))


my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
