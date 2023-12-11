def filter_string(string):
    return int(''.join([i for i in string if i.isdecimal()]))
    
print(filter_string("a1b2c3"))