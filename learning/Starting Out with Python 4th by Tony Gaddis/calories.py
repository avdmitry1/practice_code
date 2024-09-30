def calories():
    fats_grams = int(input('Enter the awount of grams of fat: '))
    carbo_grams = int(input('Enter the awount of grams of carbohydrates: '))
    return fats_grams * 9, carbo_grams * 4


calories_fat, calories_carbo = calories()

print(calories_fat, calories_carbo)
