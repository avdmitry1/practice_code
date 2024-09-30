def format_namelist(name):
    names = [i['name'] for i in name]
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return ''.join(names)
    elif len(names) == 2:
        return ' и '.join(names)
    elif len(names) >= 3:
        return ', '.join(names[:-1]) + ' и ' + names[-1]


print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
