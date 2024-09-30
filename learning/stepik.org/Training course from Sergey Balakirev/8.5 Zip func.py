# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = zip(a, b)
# res = map(lambda s: s[0] * s[1], c)
# print(next(res), next(res), next(res))

# lst_in = ['1 2 3 4 5 6', '3 4 5 6', '7 8 9', '9 7 5 3 2']

# a = zip(*(list(map(lambda x:x.split(),lst_in))))
# q = list(a)
# res = zip(*q)
# for i in res:
#     print(*i)

a = 'Python дай мне силы пройти этот курс до конца!'
res = []
zip_list = list(zip(a))
for i, v in enumerate(zip_list):
    res.append((*v, i))
print(res)