# Complete the program to find the number of combinations from n to k (values ​​are entered in the program)
# using the formula ., where . Print the result to the console as an integer using the print function.
# To calculate factorials, use the corresponding function from the math library.

import math

n, k = 6, 3


print(int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k))))