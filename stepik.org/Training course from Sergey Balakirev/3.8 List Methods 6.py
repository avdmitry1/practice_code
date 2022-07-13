# Integer numbers are entered in one line separated by a space. It is necessary to convert them to the list lst,
# then remove the last value and if it is odd, then add True to the list (at the end), otherwise - False.

numbers = list(map(int, input().split()))

last = numbers[-1]
numbers.remove(last)
numbers.append(last % 2 != 0)

print(*numbers)
