# The Fibonacci sequence is formed like this: the first two numbers are 1 and 1, and each subsequent number is equal
# to the sum of the previous two. We have the following sequence of numbers: 1, 1, 2, 3, 5, 8, 13, ...
# Construct a Fibonacci sequence of length n (n is entered from the keyboard).


num = int(input())
total = 1
i = 0
a_list = []
while num:
    i = i + total
    total, i = i, total
    a_list.append(i)
    num -= 1
print(*a_list)
