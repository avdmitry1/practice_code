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


def get_list(nums, tp=tuple()):
    def add():
        if tp == 'list':
            return [x for x in nums]
        else:
            return tuple(x for x in nums)
    return add

tp = input()
nums = list(map(int, input().split()))
lst = get_list(nums, tp)
print(lst())      