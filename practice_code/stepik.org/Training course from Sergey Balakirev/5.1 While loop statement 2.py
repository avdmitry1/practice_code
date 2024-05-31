# A positive integer n is entered. Calculate and display the sum: 1 + 1/2 + 1/3 + ... + 1/n up to thousandths
# (three decimal places).

num = int(input())
i = 1
a = []
while i <= num:
    a.append(1 / i)
    i += 1
print(round(sum(a), 3))
