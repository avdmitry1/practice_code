# # get_sq = lambda x: x ** 2
# # print(get_sq(10))


# # get_div = lambda x, y: x / y if y != 0 else None
# # print(get_div(10, 0))

# # x = float(input())
# # res = lambda x: abs(x)
# # print(res(x))


# # s = input()
# # res = lambda x: 'ra' in x
# # print(res(s))


# def filter_lst(it, key=None):
#     if key is None or key == 0:
#         return tuple(it)

#     res = ()
#     for x in it:
#         if key(x):
#             res += (x,)

#     return res

# list_nums = [int(i) for i in input().split()]
# lst = filter_lst(list_nums, lambda x: x.isinstance(x, int))
# print(*lst)
# lst = filter_lst(list_nums, lambda x: x < 0)
# print(*lst)
# lst = filter_lst(list_nums, lambda x: x >= 0)
# print(*lst)
# lst = filter_lst(list_nums, lambda x: 3 <= x <= 5)
# print(*lst)

# # здесь продолжайте программу