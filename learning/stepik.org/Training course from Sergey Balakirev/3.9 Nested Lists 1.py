# add a nested list at the end with the values entered into the program (integers are entered on the
# line separated by a space). Display the resulting list lst

nums = list(map(int, input().split()))
a = [5.4, 6.7, 10.4]
a.append(nums)

print(a)
