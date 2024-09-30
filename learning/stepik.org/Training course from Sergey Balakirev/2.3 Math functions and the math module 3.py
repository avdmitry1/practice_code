# You need to take n children and m counselors to the summer camp with the help of buses. The maximum capacity of
# each bus is 20 people. Add a program to calculate the minimum number of buses needed to transport children along
# with counselors. Print the result to the console as an integer.

import math

n, m = map(int, input().split())
print(math.ceil((n + m) / 20))
