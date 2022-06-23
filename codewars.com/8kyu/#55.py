def first_non_consecutive(arr):
    s = min(arr)
    for index, value in enumerate(arr):
        if value != s:
            return value
        s += 1


print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))
