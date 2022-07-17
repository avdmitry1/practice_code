# Write a program to find all three-digit numbers that, when divided by 47, have a remainder of 43
# and are a multiple of 3. Print the numbers found in a line separated by a space

a = 100
while a < 1001:
    if a % 47 == 43 and a % 3 == 0:
        print(a, end=' ')
    a += 1
