def feet_to_inches(feets):
    return feets * 12


num_feets = int(input('Enter number of feet: '))
print(f'In {num_feets} feet -> {feet_to_inches(num_feets)} inches')
