# a = int(input())
# b = int(input())
# c = int(input())
# print((a ** c + b ** c) ** (a * b)) 

# print(14 % -4)

# m = 153
# print(m // 60, m % 60)

# time_mins = 120
# start_hours = 19
# start_mins = 0
# hour = (time_mins + start_hours * 60 + start_mins) // 60 
# minutes = time_mins % 60 + start_mins
# print(hour if hour < 24 else int(hour - 24), minutes)

# a = 33
# b = 54
# n = 5
# hour = a * n // 60
# minutes = (a * n % 60) + (b * n // 60)
# seconds = b * n % 60
# print(hour, minutes, seconds)

# price = 100
# year_percent = 0.04
# first_pay = 50
# year_pay = 15

# first_year = int((price - first_pay - year_pay) * (1 + year_percent))
# second_year = int((first_year - year_pay) * (1 + year_percent))
# third_year = int((second_year - year_pay) * (1 + year_percent))
# print(first_year, second_year, third_year, sep='\n')

# man = 30000.50 * 100
# woman = 20000.75 * 100
# together = man + woman
# ostatok_otpusk = together * 0.1 % 1
# ostatok_food = together * 0.3 % 1
# ostatok_komunalnie = together * 0.05 % 1
# ostatok_dosug = together * 0.15 % 1
# ostatok_nakopleniya = (together * 0.4) + ostatok_otpusk + ostatok_food + ostatok_komunalnie + ostatok_dosug

# print('Отпуск:', (int(together * 0.1 // 100)), 'руб.', 
#     int(together * 0.1 % 100 - ostatok_otpusk), 'коп.')
# print('Пропитание и еда:', (int(together * 0.3 // 100)), 'руб.', 
#     int(together * 0.3 % 100 - ostatok_food), 'коп.')
# print('Коммунальные платежи:', (int(together * 0.05 // 100)), 'руб.', 
#     int(together * 0.05 % 100 - ostatok_komunalnie), 'коп.')
# print('Досуг:', (int(together * 0.15 // 100)), 'руб.', 
#     int(together * 0.15 % 100 - ostatok_dosug), 'коп.')
# print('Накопления:', (int(together * 0.4 // 100)), 'руб.', 
#     int(ostatok_nakopleniya % 100), 'коп.')

# from decimal import Decimal, getcontext
# from math import sqrt

# a = Decimal(0.1234567)
# b = Decimal(0.2345678)
# getcontext().prec = 60
# res = a.sqrt() + b
# print(res)

# import math

# a, b, c = [float(x) for x in 'abc']
# print(math.ceil(a))
# print(math.ceil(b))
# print(math.ceil(c))