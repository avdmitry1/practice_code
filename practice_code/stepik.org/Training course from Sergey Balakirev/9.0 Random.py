
# import random
# # установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
# random.seed(1)

# a = list(map(int, input().split()))
# res = random.uniform(a[0], a[1])
# print(round(res, 2))

# import random
# # установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
# random.seed(1)
# a = list(map(int, input().split()))
# res = random.randint(a[0], a[1])
# print(res)

# import random

# nums = ['1 2 3 4', '5 6 7 8', '9 8 6 7']
# res = [i.split() for i in nums]
# rnd = list(zip(*res))
# random.shuffle(rnd)
# for i in zip(*rnd):
#     print(i, end=' ')

# import random
# names = input().split()
# print(random.sample(names, 3))

