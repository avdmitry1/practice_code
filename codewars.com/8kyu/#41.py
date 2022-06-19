def abbrev_name(name):
    name = name.split()
    return f'{name[0][0].title()}.{name[1][0].title()}'


print(abbrev_name("Sam Harris"))
