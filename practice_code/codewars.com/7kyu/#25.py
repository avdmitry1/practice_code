def find_short(s):
    result = min([len(i) for i in s.split()])
    return result


print(find_short("bitcoin take over the world maybe who knows perhaps"))
