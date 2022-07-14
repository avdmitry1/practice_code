# An integer k is entered (1 <= k <= 365). Determine which day of the week (Monday, Tuesday, Wednesday, Thursday,
# Friday, Saturday or Sunday) is the k-th day of a non-leap year in which January 1 is Monday.
#


days = {1: 'понедельник', 2: 'вторник', 3: 'среда', 4: 'четверг', 5: 'пятница', 6: 'суббота', 0: 'воскресенье'}

number = int(input())
result = number % 7

print(days[result])
