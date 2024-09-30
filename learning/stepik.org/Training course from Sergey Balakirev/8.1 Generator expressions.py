# gen = (x for x in range(2, 10000)) 
# print(gen)

# a, b = map(int, input().split())

# gen = (x ** 2 for x in range(a, b))

# tp = tuple(gen)
# print(tp)

# a, b = map(int, input().split())
# gen = (abs(x) for x in range(a, b + 1))

# for i, v in enumerate(gen):
#     if i > 5:
#         break
#     else:
#         print(v)

# a = int(input())
# gen = (abs(x ** 3) for x in range(-a, a + 1))

# for i, v in enumerate(gen):
#     if i > 3:
#         break
#     else:
#         print(v, end=' ')

# from string import ascii_lowercase

# letters = ascii_lowercase
        
# gen = (j + i for j in letters for i in letters)
# for i, v in enumerate(gen, start=1):
#     if i == 51:
#         break
#     else:
#         print(v, end=' ')

# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
# gen = (i for i in range(1000000) for i in cities)
# for i, v in enumerate(gen):
#     if i == 51:
#         break
#     else:
#         print(v, end=' ')

# a, b = map(int, input().split())
# def f(x):
#     return 0.5 * pow(x/100, 2) - 2.0
# gen = (round(x, 2) for x in range(a, b))

# for i, v in enumerate(gen):
#     if i == 20:
#         break
#     else:
#         print(v, end=' ')
