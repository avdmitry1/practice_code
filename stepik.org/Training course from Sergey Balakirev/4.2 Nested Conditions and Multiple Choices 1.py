import datetime
month, date = map(int, input().split())

day = datetime.date(2021, month, date)
print(day)