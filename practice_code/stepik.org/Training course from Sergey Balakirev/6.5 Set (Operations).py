# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# result = a.symmetric_difference(b)
# print(*sorted(result))


# a = set(map(str, input().split()))
# b = set(map(str, input().split()))

# print('ДА' if a == b else 'НЕТ')


# a = set(map(int, input().split()))
# print('ДОПУЩЕН' if 2 in a else 'НЕ ДОПУЩЕН')

# a = set(map(str, input().split()))
# b = set(map(str, input().split()))
# print('ДА' if a.issubset(b) else 'НЕТ')

# a = int(input())
# print('ДА' if a % 30 == 0 else 'НЕТ')

# input_string = '1 ужасно неудовлетворительно удовлетворительно прилично отлично'.split()
# start = int(input_string[0])
# d = {i: v for i, v in enumerate(input_string[1:], start)}
# print(d)
    
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# res = len({x for x in lst_in})
# print(res)

# lst_in = list(map(str, input().lower().split()))
# result = len({x for x in lst_in if len(x) >= 3})
# print(result)


# input_string = 'И что сказать и что сказать и нечего и точка'.lower().split()
# res = dict()
# res = {v: input_string.count(input_string[i]) for i, v in enumerate(input_string)}
# print(res['и'] if 'и' in res else '0')

# lst_in = ['Пушкин: Сказака о рыбаке и рыбке', 'Есенин: Письмо к женщине', 
#           'Тургенев: Муму', 'Пушкин: Евгений Онегин', 'Есенин: Русь']
# d = {}
# x = [x.split(': ') for x in lst_in]
# for i in x:
#     d[i[0]] = d.get(i[0], {i[1]}) | {i[1]}

# print(d)
