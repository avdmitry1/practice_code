def mxdiflg(a1, a2):
    print(a1, a2)
    if len(a1) == 0 or len(a2) == 0:
        return -1
    else:
        a = len(max(a1, key=len)) - len(min(a2, key=len))
        b = len(max(a2, key=len)) - len(min(a1, key=len))
        return a if a > b else b


print(mxdiflg(["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt",
               "znnnnfqknaz", "qqquuhii", "dvvvwz"], ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]))
