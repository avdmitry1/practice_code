# sp = map(float, input().split())
# for i in range(3):
#     print(next(sp), end=' ')


# int_modul = list(map(lambda s: abs(int(s)), input().split()))
# print(int_modul)

# lst_in = ['8 11 -5', '3 4 10', '-1 -2 3', '-4 5 6']
# res = [list(map(int, x.split())) for x in lst_in]
# print(res)

# tp = tuple(map(lambda s: tuple(s.split('=')), input().split()))
# print(tp)

# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# name = 'Привет Питон'

# res = map(lambda s: t.get(s, '-'), name.lower())
# print(*list(res))


names = 'Москва Уфа Вологда Тула Владивосток Хабаровск'.split()
res = map(lambda s: '-' if len(s) <= 5 else s, names)
print(*list(res))