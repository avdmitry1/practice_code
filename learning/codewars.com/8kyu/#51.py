def human_years_cat_years_dog_years(human_years):
    c = 0
    d = 0
    for i in range(1, human_years + 1):
        if i == 1:
            c += 15
            d += 15
        elif i == 2:
            c += 9
            d += 9
        elif i > 2:
            c += 4
            d += 5
    return [human_years, c, d]


print(human_years_cat_years_dog_years(10))
