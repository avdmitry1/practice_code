# Is the string uppercase?
# Task
# Create a method to see whether the string is ALL CAPS.
import string


def is_uppercase(inp):
    if inp.isupper() or inp in string.punctuation:
        return True
    else:
        return False

print(is_uppercase("HELLO I AM DONALD"))
