# cmd = input() 

# match cmd:
#     case 'top' | 'Top' | 'TOP' as command:
#         print(f'Команда {command.lower()}')
#     case 'bottom' | 'Bottom' | 'BOTTOM' as command:
#         print(f'Команда {command.lower()}')
#     case 'right' | 'Right' | 'RIGHT' as command:
#         print(f'Команда {command.lower()}')
#     case 'left' | 'Left' | 'LEFT' as command:
#         print(f'Команда {command.lower()}')
#     case _:
#         print(f'Неверная команда')


# fio = ('Сидоров', 'Петр', 'Иванович')

# match fio:
#     case f1, f2, f3:
#         res = ", ".join([f2, f3, f1])
#     case _:
#         res = "Некорректный формат данных"

# print(res)

# student = ['Троечников С.М.', 2, 3, 3, 2, 3, 4, 3, 5, 5, 1]

# match student:
#     case fio, m1, m2, m3:               # 1-й case
#         print(f"{fio}: {m1} {m2} {m3}")
        
#     case tuple() as fio, m1, m2, m3, *_: # 2-й case
#         print(f"{fio}: {m1} {m2} {m3}")
    
#     case list() as fio, m1, m2, m3, *_: # 3-й case
#         print(f"{fio}: {m1} {m2} {m3}")
    
#     case tuple() as fio, m1, m2, m3:    # 4-й case
#         print(f"{fio}: {m1} {m2} {m3}")
    
#     case _:                             # 5-й case
#         print("Некорректный формат данных")


# book = [2, 'Зингаро. Д', 'Python без проблем', 1000.0, 2019]

# match book:
#     case int(), author, name if len(author) >= 6 and len(name) >= 10:
#         print('Yes')
#     case int(), author, name, price if len(author) >= 6 and price > 0:
#         print('Yes')
#     case int(), author, name, year if year > 2020:
#         print('Yes')
#     case int(), author, name, price, year if price > 0 and year > 2020:
#         print('Yes')
#     case _:
#         print('No')

# json_data = {'fio': 'sm_b', 'marks': [2, 2, 3, 2, 3, 4], 'age': 22}

# match json_data:
#     case {'marks': ms, 'age': age, 'fio': fio} if ms.count(2) > 1:
#         print('Ok')

# def parse_json(data):
#     match data:
#         case {'access': bool() as ac, 'data': list([date, *_])}:
#             return ac, date
#         # case {'id': ids, 'data': [_, {'login': login}, _, _]}:
#         #     return ids, login
        
#     return None


# json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}
# print(parse_json(json_data))


# def parse_json(data):
#     match data:
#         case {'data': [_, {'login': str(login), 'email': str(email)}, *_]}:
#             return login, email
#         case {'id': ids, 'data': [_, {'login': login}, *_]}:
#             return ids, login
    
#     return None

# json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}

# print(parse_json(json_data))