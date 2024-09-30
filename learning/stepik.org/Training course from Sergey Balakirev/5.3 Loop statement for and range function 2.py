# A natural number n is entered. Calculate the sum of all natural numbers less
# than n that are multiples of either 3 or 5.


number = int(input())
a_list = []
for i in range(1, number):
    a_list.append(i) if i % 3 == 0 or i % 5 == 0 else 0
print(sum(a_list))
