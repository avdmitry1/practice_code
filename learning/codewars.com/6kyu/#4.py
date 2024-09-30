def count(string):
    result = {}
    if string:
        for i, v in enumerate(string):
            result.setdefault(v, string.count(v))
        return result
    else:
        return {}


print(count(''))
