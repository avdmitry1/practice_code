import collections


def duplicate_count(text):
    res = [i for i in text.lower()]
    a = collections.Counter(res)
    result = len([i for i in a.values() if i > 1])
    return result


print(duplicate_count("abcdeaB"))
