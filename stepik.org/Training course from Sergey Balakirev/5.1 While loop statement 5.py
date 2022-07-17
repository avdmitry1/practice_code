# A natural (that is, a positive integer) number (three-digit or more) is entered. Find the product of all its digits.
# Display the result on the screen. Implement the program with a while loop.

number = int(input())
total = 1
while number:
    last = number % 10
    total *= last
    number = number // 10

print(total)