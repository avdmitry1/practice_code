def get_longest_word(s: str) -> str:
    zero = 0
    res = ''
    for i in s.split():
        if len(i) > zero:
            zero = len(i)
            res = i
    return res
