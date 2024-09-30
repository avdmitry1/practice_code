def count_positives_sum_negatives(arr):
    if not arr:
        return []
    c = 0
    n = 0
    for i in arr:
        if i > 0:
            c += 1
        elif i <= 0:
            n += i
    return [c, n]


print(count_positives_sum_negatives([0, 0]))
