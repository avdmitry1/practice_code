# Your goal is to return multiplication table for number that is always an integer from 1 to 10.


def multi_table(number):
    result = ''
    for i in range(1, 11):
        result += f'{i} * {number} = {i * number}\n'

    return result.rstrip()


print(multi_table(5))
