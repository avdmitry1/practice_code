number = int(input())
a_list = []
for i in range(1, number):
    a_list.append(i) if i % 3 == 0 or i % 5 == 0 else 0
print(sum(a_list))
