def find_keys(**x):
    lst = []
    for keys, values in x.items():
        if isinstance(values, (list, tuple)):
            lst.append(keys)
    return sorted(lst, key=str.casefold)
            
print(find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]))