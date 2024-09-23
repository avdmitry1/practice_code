# Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).

def reversed_generator(lst: list):
    for i in reversed(lst):
        yield i


nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_nums_list = list(x for x in reversed_generator(nums_list))
print(reversed_nums_list)