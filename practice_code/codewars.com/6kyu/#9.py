def order(sentence):
    index = []
    result = dict()
    sentence = sentence.split()
    for i, v in enumerate(sentence):
        for j in v:
            if j.isdigit():
                index.append(j)
    while sentence and index:
        word = sentence.pop()
        num = int(index.pop())
        result.setdefault(word, num)
    result = sorted(result, key=result.get)
    return ' '.join(result)


print(order("is2 Thi1s T4est 3a"))
