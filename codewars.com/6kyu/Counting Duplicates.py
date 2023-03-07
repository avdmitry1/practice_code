import collections


def duplicate_count(text):
    res = [i for i in text.lower()]
    a = collections.Counter(res)
    total = 0
    for i in a.values():
        if i > 1:
            total += 1

    return a, total


print(duplicate_count("abcdeaB"))
