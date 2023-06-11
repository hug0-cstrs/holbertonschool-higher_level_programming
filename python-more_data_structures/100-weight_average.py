#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:  # Check if the list is empty
        return 0

    sum_product = 0
    sum_weights = 0

    for score, weight in my_list:
        sum_product += score * weight
        sum_weights += weight

    if sum_weights == 0:  # Check if the sum of weights is zero to avoid division by zero
        return 0

    return sum_product / sum_weights
