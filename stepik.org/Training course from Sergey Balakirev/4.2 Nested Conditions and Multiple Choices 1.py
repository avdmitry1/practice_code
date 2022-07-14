import datetime

month, date = map(int, input().split())

day = datetime.date(2021, month, date)
yesterday = datetime.timedelta(days=+1)
tomorrow = datetime.timedelta(days=-1)
print(((day - yesterday).strftime("%m.%d")), ((day - tomorrow).strftime("%m.%d")))
