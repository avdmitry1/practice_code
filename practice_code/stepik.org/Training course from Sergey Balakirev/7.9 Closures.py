# def input_string(name=' '):
#     def string_strip(del_sym):
#         return del_sym.strip(name)
#     return string_strip

# f1 = input_string('?!.,:')
# f2 = input_string()

# print(f1('Kruto esli pravilno!!!!!....'), f2('  Probeli ydalit  '))


# def counter_add(num):
#     def add_5():
#         nonlocal num
#         return num + 5
#     return add_5

# k = int(input())
# f = counter_add(k)
# print(f())


# def counter_add(n):
#     def add(x):
#         return x + n 
#     return add

# k = int(input())
# cnt = counter_add(2)
# print(cnt(k))
   

# def get_tag(name):
#     def add_tag():
#         return f"<h1>{name}</h1>"
#     return add_tag

# input_name = input()
# result = get_tag(input_name)
# print(result())

# def get_tag(name, tag):
#     def add_tag():
#         return f"<{tag}>{name}</{tag}>"
#     return add_tag

# tag = input()
# input_name = input()
# result = get_tag(input_name, tag)
# print(result())


# def get_list(nums, tp=tuple()):
#     def add():
#         if tp == 'list':
#             return [x for x in nums]
#         else:
#             return tuple(x for x in nums)
#     return add

# tp = input()
# nums = list(map(int, input().split()))
# lst = get_list(nums, tp)
# print(lst())      


# def create_accumulator():
#     num = 0
#     def add(x):
#         nonlocal num
#         num += x
#         return num
#     return add

# f = create_accumulator()
# print(f(2))
# print(f(5))


# def create_accumulator(start=0):
#     def add(x):
#         nonlocal start
#         start += x
#         return start
#     return add
    
# f = create_accumulator(100)
# print(f(2))
# print(f(5))
   
# def create_dict():
#     d = {}
#     cnt = 1
#     def add(x):
#         nonlocal cnt
#         d.setdefault(cnt, x)
#         cnt += 1
#         return d
#     return add

# f = create_dict()
# print(f('Hello'))
# print(f('BTC'))
# print(f([1, 2, 3]))
    