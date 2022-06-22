def sum_str(a, b):
    if len(a) == 0 and len(b) == 0:
        return '0'
    elif len(b) == 0:
        return a
    elif len(a) == 0:
        return b
    else:
        return str(int(a) + int(b))


print(sum_str("9", "23"))
