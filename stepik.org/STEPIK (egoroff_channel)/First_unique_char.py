def first_unique_char(s):
    for i in s:
        if s.count(i) == 1:
            return s.index(i)
    return -1


print(first_unique_char('abracadabra'))
