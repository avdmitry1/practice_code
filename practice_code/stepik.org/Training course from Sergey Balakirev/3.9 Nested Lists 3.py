# A matrix of numbers of three rows is entered. In each line, the numbers are separated by a space. It is necessary
# to display the last column of this matrix as a string of three numbers separated by a space


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

print(a[-1], b[-1], c[-1])