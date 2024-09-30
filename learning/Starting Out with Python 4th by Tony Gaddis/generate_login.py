word = 'привет! меня зовут джо. а как твое имя?'
word2 = word.split()
res = ''
for i in word2:
    res += i.title() + ' '
print(res.rstrip())
