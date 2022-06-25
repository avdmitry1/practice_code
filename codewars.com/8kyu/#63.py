def index(array, n):
    if n > len(array) - 1:
        return -1
    else:
        el = array[n]
        return el ** n


print(index([1, 2, 3, 4], 2))
