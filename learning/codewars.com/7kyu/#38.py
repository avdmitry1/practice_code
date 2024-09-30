def min_value(digits):
    result = ''
    for i in sorted(digits):
        if str(i) not in result:
            result += str(i)
    return int(result)


print(min_value([1, 3, 1]))
