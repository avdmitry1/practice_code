# name = input().split()
# res = filter(lambda s: len(s) > 5, name)
# for i in range(3):
#     print(next(res), end=' ')



# city = 'зонт=1000 палатка=10000 спички=22 котелок=543'.split()

# res = tuple(map(lambda s: tuple(s.split('=')), city))
# result = filter(lambda s: s[0] if int(s[1]) > 500 else False, res)
# for i in result:
#     print(i[0], end=' ')



# nums = [8, 11, 0, -23, 140, 1]

# res = list(filter(lambda s: len(str(abs(s))) == 2, nums))
# print(*res)

# a = set(map(int,input().split()))
# b = set(map(int,input().split()))
# intersection_set = a & b
# x = sorted([x for x in intersection_set if x % 2 == 0 ])
# print(x)


# def correct_email(email):
#     if '@' in email and '.' in email:
#         допустимые_символы = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
#         остальные_символы = set(email) - {'@', '.'}
#         if остальные_символы.issubset(допустимые_символы) and email.index('@') < email.index('.'):
#             return True
#         else:
#             return False
#     else:
#         return False

# e = input().split()
# res = filter(correct_email, e)
# print(*list(res))