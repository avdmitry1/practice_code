from collections import Counter


def is_anagram(test, original):
    # print(sorted(test), sorted(original))
    # print(Counter(test), Counter(original))
    if sorted(test.lower()) == sorted(original.lower()):
        return True
    else:
        return False


print(is_anagram("foefet", "toffee"))
