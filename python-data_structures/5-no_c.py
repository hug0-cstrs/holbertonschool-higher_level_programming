#!/usr/bin/env python3
def no_c(my_string):
    translation = str.maketrans('', '', 'cC')
    return my_string.translate(translation)
