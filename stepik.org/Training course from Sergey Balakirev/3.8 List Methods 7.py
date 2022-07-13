# The student grades (numbers from 2 to 5) are entered in one line separated by a space. It is necessary to determine
# the number of twos and display this value on the screen.


numbers = list(map(int, input().split()))

print(numbers.count(2))