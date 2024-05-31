# s = input()
# lst = [int(i) for i in s.split()]
# lst.sort()
# tp_lst = tuple(sorted([int(i) for i in s.split()]))

# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}

# def get_sort(a):
#     return list(dict(sorted(a.items(), reverse=True)).values())

# print(get_sort(d))

# x = sorted([int(i) for i in input().split()], reverse=True)
# res = []
# for i in x:
#     if i not in res:
#         res.append(i)
# print(*res[:5])

# up = sorted([int(i) for i in input().split()])
# down = sorted([int(i) for i in input().split()], reverse=True)
# up_down = tuple(zip(up, down))
# res = list(map(lambda s: sum(s), up_down))
# print(*res)

# a = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']
# def func(x):
#     x = [i.split(':') for i in a]
#     d = {int(i[1]): i[0] for i in x}
#     sorted_d = sorted(d)
#     res = [d[i] for i in sorted_d]
#     return " ".join(res[:3])

# print(func(a))














