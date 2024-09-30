def get_real_floor(n):
    if n >= 13:
        return n - 2
    elif 0 < n < 13:
        return n - 1
    elif n == 0:
        return n
    else:
        return n


print(get_real_floor(-3))
