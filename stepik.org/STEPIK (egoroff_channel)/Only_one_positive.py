def only_one_positive(*arg):
    c = 0
    for i in arg:
        if i > 0:
            c += 1
    return c == 1


print(only_one_positive(1, 2))
