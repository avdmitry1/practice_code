def binary_array_to_number(arr):
    result = ''.join(str(i) for i in arr)
    return int(result, 2)


print(binary_array_to_number([1, 1, 1, 1]))
