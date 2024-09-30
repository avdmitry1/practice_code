def to_jaden_case(string):
    result = ' '.join(i.capitalize() for i in string.split())
    return result


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
