# def func_show(func):
#     def wrapper(*args):
#         res = func(*args)
#         print(f'Площадь прямоугольника: {res}')
#         return res
#     return wrapper


# @func_show
# def get_sq(width, height):
#     return width * height

# get_sq(8, 11)

# def func_show(func):
#     def wrapper(*args):
#         for i, v in enumerate(func(*args), 1):
#             print(f'{i}. {v}')
#     return wrapper
            

# @func_show
# def get_menu(s):
#     res = s.split()
#     return res
# names = 'Главная Добавить Удалить Выйти'
# print(get_menu(names))


# def dec_sort(func):
#     def wrapper(*args):
#         f = func(*args)
#         return sorted(f)
#     return wrapper



# @dec_sort
# def get_list(nums):
#     return nums

# n = [int(i) for i in input().split()]

# lst = get_list(n)
# print(*lst)


# def decor_zip(func):
#     def wrapper(*args):
#         d = {}
#         x, y = func(*args)
#         for i in range(len(x)):
#             d.setdefault(x[i], y[i])
#         print(*sorted(d.items()))
#     return wrapper


# @decor_zip
# def names(a, b):
#     return a.split(), b.split()

# a = 'house river tree car'
# b = 'дом река дерево машина'
# names(a, b)


# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# sym = {': ': '-', ' ': '-', ';': '-', '.': '-', ',': '-', '_': '-'}

# def decor(func):
#     def wrapper(*args):
#         res = func(*args)
#         lst = ''
#         for i in range(len(res)):
#             if res[i] == '-' and res[i + 1] == '-':
#                 lst += ''
#             else:
#                 lst += res[i]
#         print(lst)
#     return wrapper


# @decor
# def translate(names):
#     res = ''
#     for i in names.lower():
#         if i in t:
#             res += t[i]
#         elif i in sym:
#             res += sym[i]
#         else:
#             res += i
#     return res
# n = 'Python - это круто!'
# translate(n)


# def plus_five(start=5):
#     def decor(func):
#         def wrapper(x):
#             res = func(x) + start
#             return res
#         return wrapper
#     return decor

# @plus_five()
# def sum_nums(nums):
#     return sum(nums)

# n = [int(x) for x in input().split()]
# print(sum_nums(n))


# def add_tag(tag='div'):
#     def decor_tag(func):
#         def wrapper(x):
#             res = func(f'<{tag}>{x}</{tag}>')
#             return res
#         return wrapper
#     return decor_tag

# @add_tag(tag='div')
# def low_string(input_string):
#     return input_string.lower()

# input_str = input()
# print(low_string(input_str))


# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# import functools
# def trans_chars(chars="?!:;,. "):
#     @functools.wraps
#     def decor_chars(func):
#         def wrapper(x):
#             final = ''
#             for i in func(x):
#                 final += '-' if i in chars else i
#                 final = final.replace('--', '-')    
#             return final
#         return wrapper
#     return decor_chars


# @trans_chars()
# def trans(input_str):
#     res = ''
#     for i in input_str.lower():
#         res += t[i] if i in t else i
#     return res
# s = 'Декораторы - это круто!'
# print(trans(s))
# print(trans.__name__)

# from functools import wraps

# def sum_main(func):
#     @wraps(func)
#     def wrapper(x):
#         res = func(x)
#         return sum(res)
#     return wrapper

# @sum_main
# def get_list(nums):
#     '''Функция для формирования списка целых значений'''
#     res = [int(x) for x in nums.split()]
#     return res

# print(get_list("1 2 3 -1 -2 -3"))
# print(get_list.__name__)
# print(get_list.__doc__)
    

# d = int(input())
# d_list = []
# for i in range(d):
#     words = input()
#     d_list.append(words)

# l = int(input())
# l_list = []
# for i in range(l):
#     words2 = input().lower()
#     l_list.append(words2)
    
# errors = set()
# for i in l_list:
#     for j in i.split():
#         if j.lower() not in d_list:
#             errors.add(j.lower())

# for x in errors:
#     print(x)
