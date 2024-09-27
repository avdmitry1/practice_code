import calendar

print(calendar.calendar(2024)) # Returns a year's calendar as a multi-line string.
print("------------------------------------------------------------------------")
print(calendar.month(2024, 9)) #Return a month's calendar string (multi-line).
print("------------------------------------------------------------------------")
print(calendar.isleap(2024)) # Return True for leap years, False for non-leap years.
print("------------------------------------------------------------------------")
print(calendar.leapdays(1987, 2024)) #Return number of leap years in range [y1, y2) 
print("------------------------------------------------------------------------")

import bisect

a = [1, 3, 4, 5, 7]
x = 4
position = bisect.bisect_left(a, x) # Return the index where to insert item x in list a, assuming a is sorted.
print(position) # element x can be inserted at index 2 before element with this value
bisect.insort_left(a, x) # Insert item x in list a, and keep it sorted assuming a is sorted.
print(a)  # [1, 3, 4, 4, 5, 7]
# Interval boundaries
boundaries = [10, 20, 30, 40, 50]
value = 36

# Searching for the interval index
index = bisect.bisect_right(boundaries, value) #Return the index where to insert item x in list a, assuming a is sorted.
print(f"Value {value} falls within the interval, from {boundaries[index-1]} to {boundaries[index]}")