# Напишіть функцію-генератор для отримання n перших простих чисел.

def is_simple_num_generator(lst: list):
    for i in range(2, len(lst) + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i
nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
is_simple_num = list(x for x in is_simple_num_generator(nums_list))
# print(is_simple_num)