def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr else 0


print(sum_array([3, 2, 44, 5, 66]))
