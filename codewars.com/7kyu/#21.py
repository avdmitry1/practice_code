def number(lines):
    return [f"{index}: {value}" for index, value in enumerate(lines, 1)]


print(number(["a", "b", "c"]))
