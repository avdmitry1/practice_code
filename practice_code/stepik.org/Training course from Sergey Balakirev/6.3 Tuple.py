# t = (3.4, -56.7)
# num_tuple = tuple(map(int, input().split()))

# print(t + num_tuple)


# cities = tuple(input().split())
# city = ('Львов',)
# print(' '.join(cities + city if city[0] not in cities else cities))
# # if city[0] not in cities:
# #     res = cities + city
# #     print(' '.join(res))
# # else:
# #     print(' '.join(cities))

# cities = tuple(input().split())
# city_to_remove = 'Ульяновск'
# result = ''.join(tuple(x for x in cities if x != city_to_remove))
# print(result)


# names = tuple(input().lower().split())
# name_to_find = 'ва'
# result = ' '.join(tuple(x for x in names if name_to_find in str(x)))
# print(result)

# nums = tuple(map(int, input().split()))
# uniqe_nums = [i for i, v in enumerate(nums) if nums.count(v) > 1]
# # for i, v in enumerate(nums):
# #     if nums.count(v) > 1:
# #         uniqe_nums.append(i)
# print(uniqe_nums)
    
    
# n = int(input())
# lst = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
# for i in lst:
#     print(*i)

lst_in = ['Главная home', 'Python learn-python', 'Java learn-java', 'PHP learn-php']
lst = tuple([tuple(map(str, v.split())) for v in lst_in])
print(lst)