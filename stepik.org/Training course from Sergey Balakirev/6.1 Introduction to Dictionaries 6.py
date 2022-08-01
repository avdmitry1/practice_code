number = int(input())
d = {}

while number != 0:
    if number not in d:
        d[number] = round(number ** 0.5, 2)
        print(d[number])
    else:
        print('значение из кэша:', d[number])
    number = int(input())
