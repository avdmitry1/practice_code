def least_larger(a, index):
    for i in a:
        if i == a[index] + 1:
            return a.index(i)
    return -1


print(least_larger([4, 1, 3, 5, 6], 0))
