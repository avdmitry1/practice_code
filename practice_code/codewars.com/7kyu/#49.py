# Task
# Given an array of positive integers (the weights of the people), return a new array/tuple of two integers,
# where the first one is the total weight of team 1, and the second one is the total weight of team 2.


def row_weights(array):
    return sum(array[0::2]), sum(array[1::2])


print(row_weights([50, 60, 70, 80]))
