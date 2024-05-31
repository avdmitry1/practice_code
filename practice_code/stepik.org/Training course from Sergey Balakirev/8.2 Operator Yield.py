# N = int(input())

# def get_sum():
#     for i in range(1, N + 1):
#         a = range(1, i + 1)
#         yield sum(a)

# gen = get_sum()
# for x in gen:
#     print(x, end=' ')



# def get_f(N):
#     fibo = [1, 1, 1]
#     while len(fibo) < N:
#         fibo.append(fibo[-1] + fibo[-2] + fibo[-3])
#     yield fibo
    
# N = int(input())

# gen = get_f(N)
# for x in gen:
#     print(*x, end=' ')

# from string import ascii_lowercase, ascii_uppercase
# import random

# N = int(input())

# random.seed(1)

# chars = ascii_lowercase + ascii_uppercase

# def rand_pass(N):
#     for x in range(N):
#         password = ''
#         for i in range(N):
#             password += random.choice(chars)
#         yield password + '@mail.ru'

# res = rand_pass(N)
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))


# def get_simple_numbers(n=2):
#     while True:
#         if all((n % i) for i in range(2, int(n ** 0.5) + 1)):
#             yield n
#         n += 1
        
# gen = get_simple_numbers()
# print(*(next(gen) for _ in range(20)))