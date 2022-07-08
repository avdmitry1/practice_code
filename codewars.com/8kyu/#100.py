# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.
#
# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.
#
# Your function will be tested with pre-made examples as well as random ones.

def find_difference(a, b):
    a1 = 1
    b1 = 1
    for i in a:
        a1 *= i
    for i in b:
        b1 *= i
    return abs(a1 - b1)


print(find_difference([3, 2, 5], [1, 4, 4]))
