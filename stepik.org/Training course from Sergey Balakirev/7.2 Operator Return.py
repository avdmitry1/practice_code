# def square(num: float) -> float:
#     return num ** 2
# number = float(input())
# print(square(number))

# def is_triangle(a, b, c : int) -> bool:
#     if a < b + c and b < a + c and c < a + b:
#         return True
#     else:
#         return False
# a, b, c = list(map(int, input().split()))
# print(is_triangle(a, b, c))

# def is_large(input_string: str) -> bool:
#     return True if len(input_string) > 3 else False
# input_string = input()
# print(is_large(input_string))

# def even(num: int):
#     return True if num % 2 == 0 else False

# input_num = 0
# while input_num != 1:
#     input_num = int(input())
#     if even(input_num):
#         print(input_num) 


# def odd(num: int):
#     return True if num % 2 != 0 else False

# numbers = list(map(int, input().split()))
# result = [x for x in numbers if odd(x)]
# print(*result)


# tp = input().strip()
# if tp == 'RECT':
#     def get_sq(a, b=None):
#         return a * b
# elif tp != 'RECT':
#     def get_sq(a, b=None):
#         return a * a
    

# def len_string(input_string: str):
#     if len(input_string) >= 6:
#         return True
    
# city_names = list(input().split())
# lst = [x for x in city_names if len_string(x)]
# print(*lst)

# def string_len(input_string: str) -> tuple:
#     return input_string, len(input_string)

# city_names = input().split()
# d = {string_len(x)[0]: string_len(x)[1] for x in city_names}
# a = sorted({string_len(x)[0]: string_len(x)[1] for x in city_names}, key=lambda x: d[x])
# print(a)


# numbers = list(map(int, input().split()))
# def multi(a: int, b: int):
#     return a * b
# result = multi(max(numbers), min(numbers))
# print(result)

# def get_nod(a, b):
#     if a < b:
#         b, a = a, b
#     while b != 0:
#         a, b = b, a % b
#     return a
# print(get_nod(14, 240))