def count_strings(*x):
    res = 0
    for i in x:
        if isinstance(i, str):
            res += 1
    return res

print(count_strings('am', 'world', 'hello', 'is'))