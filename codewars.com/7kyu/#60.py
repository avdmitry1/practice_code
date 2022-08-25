# This time no story, no theory. The examples below show you how to write function accum:
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

# noinspection PyTypeChecker
def accum(s):
    y = ''
    for i in range(len(s)):
        y += s[i].lower() * (i + 1) + "-"
    return y.title()[:-1]


print(accum("ZpglnRxqenU"))
