def format_namelist(name):
    result = ''
    names = [i['name'] for i in name]
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return ''.join(names)
    elif len(names) == 2:
        return ' и '.join(names)
    elif len(names) >= 3:
        for i in names[:-2]:
            result += i + ', '.join(names[:-2])
        return result + names[-2] + ' и ' + names[-1]


print(format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'}]))
