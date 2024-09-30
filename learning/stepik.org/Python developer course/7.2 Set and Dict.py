# def cnt(number: int) -> int:
#     res = set()
#     res.add(number)
#     while number != 0:
#         number = int(input())
#         res.add(number)
#     return len(res)
# number = int(input())
# print(cnt(number))

# def square(a: set) -> list:
#     res = sum([i ** 2 for i in a])
#     return res
# a = {int(i) for i in input().split()}
# print(square(a))

# lst = input().split()
# set_lst = lst
# for i in sorted(list(set_lst)):
#     print(i, lst.count(i))            

# d = [{
#         "id": 1,"parents": [1,2,3,4],"chief": {"name": "Paul","age": 50},"age": 92
#     }, 
#     {
#         "id": 1,"parents": [1,2,3,4],"chief": {"name": "Paul","age": 62},"age": 80
#      }]
# max_age = 0
# for i in d:
#     for k, v in i.items():
#         if i['chief']['age'] > max_age:
#             max_age = i['chief']['age']
#         elif k == 'age':
#             if i['age'] > max_age:
#                 max_age = i['age']
#         else:
#             max_age
# print(max_age)
        

# data = {"version": 2, "authors": ["Anton", "Andrey"]}

# match data:
#     case {"version": 1, "author": name}:
#         print(name) # Anton
#     case {"version": 2, "authors": [*names]}:
#         print(*names)
#     case _:
#         print('Неизвестная версия')
        
# d = {}
# mass = ['a', 'a', 'b', 'b', 'b', 'c']
# # Вариант без defaultdict
# for i in mass:
#     if not d.get(i):
#         d[i] = 0
#     d[i] += 1
# print(d) # {'a': 2, 'b': 3, 'c': 1}
# # С использованием defaultdict
# from collections import defaultdict
# d = defaultdict(int) # значение по умолчанию 0
# for i in mass:
#     d[i] += 1
# print(d) # defaultdict(<class 'int'>, {'a': 2, 'b': 3, 'c': 1})


# d = {}
# mass = ['a', 'a', 'b', 'b', 'b', 'c']
# # Вариант без Counter
# for i in mass:
#     if not d.get(i):
#         d[i] = 0
#     d[i] += 1
# print(d) # {'a': 2, 'b': 3, 'c': 1}
# # С использованием Counter
# from collections import Counter
# d = Counter(mass)
# print(d) # Counter({'b': 3, 'a': 2, 'c': 1})
# # список из наиболее распространенных элементов (можно ограничить количество параметром)
# print(d.most_common())  # [('b', 3), ('a', 2), ('c', 1)]

# from collections import Counter, defaultdict
# urls, statuses = defaultdict(int), defaultdict(int)
# income = input()
# request, http_code = income.split()
# while income != 'end':
#     request, http_code = income.split()
#     urls[request] += 1
#     statuses[http_code] += 1
#     income = input()
# for k, v in sorted(statuses.items()):
#     print(k, v)
# for j, l in sorted(urls.items()):
#     print(j, l)



    