def dig_pow(n, p):
    range_num = 0
    for i in str(n):
        range_num += int(i) ** p
        p += 1  
    if range_num % n == 0:
        return range_num // n
    else:
        return -1

print(dig_pow(46288, 3))