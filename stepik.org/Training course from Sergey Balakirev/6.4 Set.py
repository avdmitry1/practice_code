# set_nums = set(map(float, input().split()))
# print(*sorted(set_nums))

# set_words = set(map(str, input().lower().split()))
# print(len(set_words))

# words = 'Python 3.9.11 - best language!'
# result = set()
# if any(i.isdigit() for i in words):
#     for i in words.split():
#         for j in i:
#             if j.isnumeric():
#                 result.add(j)
#     print(*sorted(result))
# else:
#     print('НЕТ')


start_end = input()
cities = set()
while start_end != 'q':
    cities.add(start_end)
print(cities)