import string


def alphabet_position(text):
    result = ''
    for i, v in enumerate(text.lower()):
        for j, k in enumerate(string.ascii_lowercase, 1):
            if k in v:
                result += str(j) + ' '
    return result.rstrip(' ')


print(alphabet_position("The sunset sets at twelve o' clock."))
