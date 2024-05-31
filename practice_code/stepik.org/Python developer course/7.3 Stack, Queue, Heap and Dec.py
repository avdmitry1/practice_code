# lst = []
# num = int(input())
# while num != -1:
#     lst.append(num)
#     num = int(input())
    
    
# for i in reversed(lst):
#     print(i)

# stack = []
# while True:
#     command = input()
#     if command == 'close':
#         break
#     if command == 'head':
#         print(stack[-1])
#     if command[:3] == 'add':
#         stack.append(int(command[3:]))
#     if command == 'pop' and len(command) > 0:
#         print(stack.pop())


# from collections import deque

# deq = deque()
# while True:
#     command = input()
#     if command == 'close':
#         break
#     elif command == 'head':
#         print(deq[-1])
#     elif command[:3] == 'add':
#         deq.appendleft(int(command[3:]))
#     elif command == 'pop':
#         print(deq.pop())

# from itertools import cycle, chain, combinations

# for idx, value in enumerate(cycle('abcd')):  # создать бесконечный итератор по буквам
#     print(value, idx)
#     if idx > 10:
#         break

# d = {'a': '1', 'b': '2', 'c': '3'}
# s = 'abacaba'
# table = s.maketrans(d)
# print(table)
# print(s.translate(table))

# class Stack:
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return self.items == []
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         return self.items.pop()
#     def peek(self):
#         return self.items[len(self.items)-1]
#     def size(self):
#         return len(self.items)
#     def __str__(self):
#         return f'{self.items}'


# class Queue(object):
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return self.items == []
#     def enqueue(self, item):
#         self.items.insert(0, item)
#     def dequeue(self):
#         return self.items.pop()
#     def size(self):
#         return len(self.items)
#     def __str__(self):
#         return f'{self.items}'
    
# queue = Queue()
# queue.enqueue('White')
# queue.enqueue('Green')
# queue.enqueue('Black')
# print(queue)
# queue.dequeue()
# print(queue)


# def BubbleSort(lst):
#     lastIndx = len(lst) - 1
#     for i in range(lastIndx, 0, -1):
#         for idx in range(i):
#             if lst[idx] > lst[idx + 1]:
#                 lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
#     return lst

# print(BubbleSort([2, 5, 1, 2, 6, 9, 4, 3]))

import Circle
import Rectangle

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5


def main():
    choice = 0

    while choice != QUIT_CHOICE:
        # Показать меню
        display_menu()
        # Получить вариант выбора пользователя
        choice = int(input('Введите вариант: '))
        # Выполнить выбранное действие
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input('Введите радиус круга: '))
            print('Площадь равна', Circle.area(radius))

        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input('Введите радиус круга: '))
            print('Длинна окружности равна', Circle.circumference(radius))

        elif choice == AREA_RECTANGE_CHOICE:
            width = float(input('Введите ширину прямоугольника: '))
            length = float(input('Введите длину прямоугольника: '))
            print('Площадь равна', Rectangle.area(width, length))

        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input('Введите ширину прямоугольника: '))
            length = float(input('Введите длину прямоугольника: '))
            print('Периметр равен', Rectangle.perimeter(width, length))

        elif choice == QUIT_CHOICE:
            print('Выходим из программы')
        else:
            print('Ошибка, недопустимый выбор')

# Функция дисплей показывает меню


def display_menu():
    print('MENU')
    print('1. Площадь круга')
    print('2. Длина окружности')
    print('3. Площадь прямоугольника')
    print('4. Периметр прямиоугольника')
    print('5. Выход')


main()