# Two natural even numbers n and m are entered in one line separated by a space, and n < m. Print all odd numbers
# from the interval [n, m]. Solve the problem without using a conditional operator.

a, b = map(int, input().split())
result = a + 1
while result < b:
    print(result, end=' ')
    result += 2
