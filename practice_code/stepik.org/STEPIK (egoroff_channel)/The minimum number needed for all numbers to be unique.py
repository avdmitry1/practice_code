numbers = list(map(int, input().split()))
x = len(numbers)
y = len(set(numbers))
print(x - y)