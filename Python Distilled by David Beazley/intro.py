def filter_string(string):
    new = [i for i in string if i.isdecimal()]
    return int(''.join(new))
    
print(filter_string("a1b2c3"))