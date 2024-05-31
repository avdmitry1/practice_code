# The date of a certain day is characterized by two natural numbers: m (serial number of the month) and n (number).
# According to the entered m and n (in one line separated by a space), determine:
# a) the date of the previous day (assume that m and n do not characterize January 1);
# b) the date of the next day (assume that m and n do not characterize December 31).
# The problem is to assume that the year is not a leap year. Output the previous date and the next date (in the
# format: mm.dd, where m is the day of the month; d is the number of the day) in one line separated by a space.
#
# P.S. Number of days in non-leap year months starting from January: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

import datetime

month, date = map(int, input().split())

day = datetime.date(2021, month, date)

yesterday = datetime.timedelta(days=+1)
tomorrow = datetime.timedelta(days=-1)

print((day - yesterday).strftime("%m.%d"), (day - tomorrow).strftime("%m.%d"))
