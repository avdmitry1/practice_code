def round_to_next5(n):
    while n:
        if n % 5 == 0:
            break
        n += 1
    return n


print(round_to_next5(12))
