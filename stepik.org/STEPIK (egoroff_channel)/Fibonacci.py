a = 0
b = 1
n = int(input())
for __ in range(n):
    a, b = b, a + b
print(a)
