MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    print(f'{name} еще рано садиться за руль' if age < MIN_DRIVING_AGE else f'{name} может водить')


allowed_driving('tim', 17)
