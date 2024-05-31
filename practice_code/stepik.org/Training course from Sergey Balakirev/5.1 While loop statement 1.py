# Enter the cost of one book x rubles (real number). It is necessary to display on the screen the cost of 2, 3, ... 10
# such books separated by a space, accurate to tenths.

price = float(input())
i = 2
while i < 11:
    print(round(price * i, 1), end=' ')
    i += 1
