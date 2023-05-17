baseball = set(['Джоди', 'Кармен', 'Аида', 'Алисия'])
basketball = set(['Ева', 'Кармен', 'Алисия', 'Сара'])

print('Студенты которые играют в баскетбол и бейсбол')
for name in baseball.intersection(basketball):
    print(name)
print('-' * 15) 
   
print('Эти студенты играют в одну или обе игры')
for name in baseball.union(basketball):
    print(name)
print('-' * 15)

print('Эти студенты играют в бейсбол, но не в баскетбол')
for name in baseball.difference(basketball):
    print(name)
print('-' * 15)

print('Эти студенты играют в баскетбол, но не в бейсбол')
for name in basketball.difference(baseball):
    print(name)
print('-' * 15)

print('Эти студенты играют в одну из спортивных игра, но не в обе')
for name in baseball.symmetric_difference(basketball):
    print(name)
print('-' * 15)

    
