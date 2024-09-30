# Complete the function that receives as input a string, and produces outputs according to the following table:

def get_drink_by_profession(param):
    if param.title() == 'Jabroni':
        return "Patron Tequila"
    elif param.title() == "School Counselor":
        return "Anything with Alcohol"
    elif param.title() == "Programmer":
        return 'Hipster Craft Beer'
    elif param.title() == 'Bike Gang Member':
        return "Moonshine"
    elif param.title() == 'Politician':
        return "Your tax dollars"
    elif param.title() == 'Rapper':
        return "Cristal"
    else:
        return "Beer"


print(get_drink_by_profession('jabrOni'))
