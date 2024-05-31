# Integer numbers are entered in one line separated by a space (at least four). You need to find the three smallest
# numbers in this sequence of numbers and display them in ascending order. Execute the program without using a
# conditional statement.

numbers = list(map(int, input().split()))
numbers.sort()

print(*numbers[:3])
