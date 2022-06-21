def binary_array_to_number(arr):
    x = [str(i) for i in arr]
    result = ''.join(x)
    return int(result, 2)


print(binary_array_to_number([1, 1, 1, 1]))
