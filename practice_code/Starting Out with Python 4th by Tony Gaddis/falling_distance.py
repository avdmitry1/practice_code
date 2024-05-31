def falling_distance(time):
    result = (1 / 2) * 9.8 * (time ** 2)
    return result


for i in range(1, 11):
    print(f'{falling_distance(i):,.2f}')
