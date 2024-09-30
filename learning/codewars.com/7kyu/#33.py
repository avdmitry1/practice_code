def descending_order(num):
    result = ''
    for i in (sorted(str(num), reverse=True)):
        result += i
    return int(result)


print(descending_order(15))
