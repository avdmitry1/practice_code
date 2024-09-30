def find_duplicate(data):
    result = []
    for i in data:
        if i not in result and data.count(i) > 1:
            result.append(i)
    return result
