# A natural number N is entered (that is, a positive integer). It is required to create a two-dimensional (nested)
# list of N x N elements, consisting of all ones, and then write fives in the last column. Display this list on the
# screen as a table of numbers, as shown in the example below.
#
# P.S. Be careful there should be no spaces at the end of the lines!

num = int(input())
a_list = []
for i in range(num):
    a_list.append(['1 '] * num)
for i in range(num):
    a_list[i][-1] = '5'
for i in a_list:
    print()
    for j in i:
        print(j, end='')
