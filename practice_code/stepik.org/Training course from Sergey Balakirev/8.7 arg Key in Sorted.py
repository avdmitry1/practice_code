# my_list = ['apple', 'banana', 'kiwi', 'orange']
# sorted_list = sorted(my_list, key=len)
# print(sorted_list)

# my_list = ['apple', 'banana', 'kiwi', 'orange']
# sorted_list = sorted(my_list, key=lambda x: x[-1])
# print(sorted_list)

# my_list = [-5, 2, -10, 8, -3]
# sorted_list = sorted(my_list, key=abs)
# print(sorted_list)
# Вывод: [2, -3, -5, 8, -10]

# my_dict = {'apple': 5, 'banana': 2, 'kiwi': 8, 'orange': 3}
# sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
# print(sorted_dict)
# # Вывод: {'banana': 2, 'orange': 3, 'apple': 5, 'kiwi': 8}

# my_tuples = [(1, 5), (3, 2), (2, 8), (4, 3)]
# sorted_tuples = sorted(my_tuples, key=lambda x: x[1])
# print(sorted_tuples)
# # Вывод: [(3, 2), (4, 3), (1, 5), (2, 8)]

# my_strings = ['AABBbc', 'DeFg', 'hIJ', 'kLmN']
# sorted_strings = sorted(my_strings, key=lambda x: sum(1 for char in x if char.isupper()))
# print(sorted_strings)
# # Вывод: ['DeFg', 'hIJ', 'kLmN', 'AABBbc']

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
# sorted_people = sorted(people, key=lambda x: x.age)
# for person in sorted_people:
#     print(person.name, person.age)
# # Вывод: Bob 25, Alice 30, Charlie 35

# students = [
#     {'name': 'Alice', 'grade': 85, 'age': 21},
#     {'name': 'Bob', 'grade': 92, 'age': 20},
#     {'name': 'Charlie', 'grade': 88, 'age': 22}
# ]
# sorted_students = sorted(students, key=lambda x: (x['name']))
# for student in sorted_students:
#     print(student['name'], student['grade'], student['age'])
# # Вывод: Alice 85 21, Charlie 88 22, Bob 92 20

# from datetime import datetime

# dates = ['2022-02-01', '2022-01-15', '2022-03-05']
# sorted_dates = sorted(dates, key=lambda x: datetime.strptime(x, '%Y-%m-%d'))
# print(sorted_dates)
# # Вывод: ['2022-01-15', '2022-02-01', '2022-03-05']

# numbers = [234, 56, 987, 1234]
# sorted_numbers = sorted(numbers, key=lambda x: sum(int(digit) for digit in str(x)))
# print(sorted_numbers)
# # Вывод: [234, 1234, 56, 987]

# strings = ['abc123', 'def4564', 'ghi78', 'jklm']
# sorted_strings = sorted(strings, key=lambda x: sum(1 for char in x if char.isdigit()))
# print(sorted_strings)
# # Вывод: ['jklm', 'ghi78', 'abc123', 'def4564']

# strings = ['apple', 'Banana', 'Orange', 'kiwi']
# sorted_strings = sorted(strings, key=lambda x: len(x.lower()))
# print(sorted_strings)
# # Вывод: ['kiwi', 'apple', 'Banana', 'Orange']

# strings = ['hello', 'world', 'python', 'programming']
# sorted_strings = sorted(strings, key=lambda x: len(set(x)))
# print(sorted_strings)
# # Вывод: ['hello', 'world', 'python', 'programming']


# tuples = [(2, 5), (7, 3), (10, 12), (6, 6)]
# sorted_tuples = sorted(tuples, key=lambda x: abs(x[0] - x[1]))
# print(sorted_tuples)
# # Вывод: [(6, 6), (10, 12), (2, 5), (7, 3)]

# data = [{'a': 10, 'b': 20}, {'a': 5, 'b': 15}, {'a': 8, 'b': 12}]
# sorted_data = sorted(data, key=lambda x: (x['a'] + x['b']) / 2)
# print(sorted_data)
# # Вывод: [{'a': 5, 'b': 15}, {'a': 8, 'b': 12}, {'a': 10, 'b': 20}]

# strings = ['apple', 'banana', 'kiwi', 'orange']
# sorted_strings = sorted(strings, key=lambda x: x.count('a'))
# print(sorted_strings)
# # Вывод: ['kiwi', 'apple', 'orange', 'banana']


# name = 'Лена Енисей Волга Дон'.split()
# reversed_name = sorted(name, key=len, reverse=True)
# print(*reversed_name)

# lst_in = ['ножницы=100', 'котелок=500', 'спички=20', 'зажигалка=40', 'зеркальце=50']
# tp = tuple(x.split('=') for x in lst_in)
# res = sorted(tp, key=lambda x: int(x[1]), reverse=True)
# for name in res:
#     print(name[0], end=' ')

# n = ("до", "ре", "ми", "фа", "соль", "ля", "си")
# notes = 'до фа соль до ре фа ля си'.split()
# res = sorted(notes, key=lambda s: n.index(s))
# print(*res)

