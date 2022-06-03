# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    s = [i for i in s if i != '!']
    s = ''.join(s)
    return s

    # return s.replace('!', '')


print(remove_exclamation_marks("Hello World!"))
