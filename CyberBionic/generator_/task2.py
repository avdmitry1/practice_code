# Виведіть із списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: генератор та цикл

def square_nums_generator(lst: list):
    for i in lst:
        yield i ** 2 if i % 2 == 0 else None 


nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_nums_list = list(x for x in square_nums_generator(nums_list) if x is not None)
print(square_nums_list)