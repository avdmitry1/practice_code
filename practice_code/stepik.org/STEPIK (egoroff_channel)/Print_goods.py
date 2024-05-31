def print_goods(*goods):
    count, result = 1, ''
    for i in goods:
        if isinstance(i, str) and len(i) > 0:
            result += f'{count}. {i}\n'
            count += 1
    if count == 1:
        result += 'Нет товаров'
    print(result)


print_goods('apple', 'banana', 'orange')
