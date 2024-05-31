# Write a simple regex to validate a username. Allowed characters are:
#
# lowercase letters,
# numbers,
# underscore
# Length should be between 4 and 16 characters (both included).
import string


def validate_usr(username):
    c = 0
    if not 4 <= len(username) <= 16:
        return False
    for i in username:
        if i in string.ascii_lowercase or i.isdigit() or i == '_':
            c += 0
        else:
            c += 1
    return True if c == 0 else False


print(validate_usr('Pfmnty0r6db'))
