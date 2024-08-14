def weekend(day: str) -> bool:
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    weekend_days = ['Saturday', 'Sunday']
    if day in weekdays:
        return "Сьогодні на роботу"
    elif day in weekend_days:
        return "Сьогодні вихідний"
    else:
        return "Такого дня не існує"
    
input_day = input("Введіть день: ")
print(weekend(input_day))