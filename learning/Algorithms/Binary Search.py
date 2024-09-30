def binary_search(l1st, item):
    # Declaring search boundaries - обьявляем границы поиска
    low = 0
    high = len(l1st) - 1
    print(high)
    while low <= high:
        # Finding the middle element - Находим средний элемент
        mid = (low + high) // 2
        guess = l1st[mid]
        print(f'Мин граница - {low} | Макс граница - {high} | Средний индекс - {mid} |')
        # Found a number and return his index - Нашли число и возвращаем его индекс
        if guess == item:
            return mid
        # The number is more than required - Число больше нужного
        if guess > item:
            high = mid - 1
        # The number is less than required - Число меньше нужного
        else:
            low = mid + 1
    # Value is not in the list - Значение отсутствует в списке
    return None


lst = [1, 2, 3, 6, 8, 9, 10, 14, 21]
print(binary_search(lst, 1))
