#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = (len(sentence), sentence[0])
    if sentence is None:
        tuple_empty = (len(sentence), None)
        return tuple_empty
    return new_tuple
