# def first_func():
#     print("It's my first function")
# first_func()

# def input_name():
#     name = input()
#     print(f'Уважаемый, {name}! Вы верно выполнили это задание!')
# input_name()

# def func(weight):
#     print(f'Предмет имеет вес: {weight} кг.')
    
# func(float(input()))

# def func(nums):
#     v_min = min(nums)
#     v_max = max(nums)
#     v_sum = sum(nums)
#     print(f"Min = {v_min}, max = {v_max}, sum = {v_sum}")
# func(list(map(int, input().split())))

# def rectangle(width, height):
#     x = 2 * (width + height)
#     print(f'Периметр прямоугольника, равен {x}')
# w, h = list(map(int, input().split()))
# rectangle(w, h)


# def correct_email(email):
#     if '@' in email and '.' in email:
#         допустимые_символы = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
#         остальные_символы = set(email) - {'@', '.'}
        
#         if остальные_символы.issubset(допустимые_символы):
#             print("ДА")
#         else:
#             print("НЕТ")
#     else:
#         print("НЕТ")
# e = input()
# print(correct_email(e))
