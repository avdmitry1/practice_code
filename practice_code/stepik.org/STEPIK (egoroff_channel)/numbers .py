numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = list(map(lambda x: x ** 2, numbers))
cube = list(map(lambda x: x ** 3, numbers))

print(square, cube, sep="\n")