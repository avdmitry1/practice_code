import random as rnd


def math_test():
    r = rnd.randint(1, 100)
    r2 = rnd.randint(1, 100)
    print(r)
    print(r2)

    answer = int(input('Enter your answer -> '))
    if answer == r + r2:
        print('Congratulations ;)')
    else:
        print('WRONG ANSWER!')


math_test()
