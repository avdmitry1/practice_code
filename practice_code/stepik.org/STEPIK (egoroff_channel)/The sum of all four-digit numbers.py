# the sum of all four-digit numbers, the sum of the digits of each of which is 20
def sum_digit(number):
    c = 0
    while number > 0:
        c += number % 10
        number //= 10
        print(c)
    return c


p = 0
for i in range(1000, 10000):
    if sum_digit(i) == 20:
        p += i
print(p)
