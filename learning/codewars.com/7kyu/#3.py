# Implement a function that adds two numbers together and returns their sum in binary.
# The conversion can be done before, or after the addition.
#
# The binary number returned should be a string.
#
#

def add_binary(a, b):
    s = a + b
    result = ""
    while s > 0:
        x = str(s % 2)
        result += x
        s = int(s // 2)

    return result[::-1]


print(add_binary(51, 12))
