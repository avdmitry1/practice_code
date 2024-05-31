
# nums = list(map(int, input().split()))
# print(all([True for x in nums if x % 2 == 0]))

# text = "hello world"
# print(all(char.islower() for char in text))  
# # Вернет True, так как все символы в строке в нижнем регистре


# words = ["apple", "banana", "strawberry", "watermelon", "orange"]
# print(any(len(word) > 10 for word in words))  
# # Вернет True, так как есть слово длиной больше 10 символов




# nums = list(map(int, input().split()))
# print(any([x < 0 for x in nums]))

# def is_string(lst):
#     res = all([type(x) is str for x in lst])
#     return res

# nums = list(map(int, input().split()))
# print('отчислен' if any([x < 3 for x in nums]) else 'учится')


# def is_free(lst):
#     res = any(['#' in i for i in lst])
#     return res

# print(is_free(['# x o', 'x # x', 'o o #']))
